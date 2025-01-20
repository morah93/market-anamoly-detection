import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Card,
  Container,
  Grid,
  Typography,
  CircularProgress,
  List,
  ListItem,
  ListItemText,
  Box,
} from '@mui/material';
import {
  Timeline,
  Warning,
  TrendingUp,
  Assessment
} from '@mui/icons-material';

const MarketDashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  // const fetchData = async () => {
  //   try {
  //     const response = await fetch('http://localhost:5000/api/market-analysis');
  //     if (!response.ok) {
  //       throw new Error(`HTTP error! status: ${response.status}`);
  //     }
  //     const result = await response.json();
  //     setData(result);
  //   } catch (error) {
  //     setError(`Fetch error: ${error.message}`);
  //   } finally {
  //     setLoading(false);
  //   }
  // };

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/market-analysis');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const result = await response.json();
      console.log('API response:', result); // Add this for debugging
      setData(result);
      // console.log(result)
    } catch (error) {
      console.error('Fetch error:', error); // Add this for debugging
      setError(`Fetch error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };


  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  const marketRisk = data?.market_risk;

  if (!marketRisk) {
    return <div>Market risk data is not available.</div>;
  }

  const getRiskColor = (riskLevel) => {
    const colors = {
      'Low': '#4caf50',
      'Medium': '#ff9800',
      'High': '#f44336',
      'Very High': '#d32f2f'
    };
    return colors[riskLevel] || '#000';
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Market Analysis Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* Risk Assessment Card */}
        <Grid item xs={12} md={6}>
          <Card sx={{ p: 3 }}>
            <Box display="flex" alignItems="center" mb={2}>
              <Warning sx={{ mr: 1 }} />
              <Typography variant="h6">Risk Assessment</Typography>
            </Box>
            <Typography variant="h4" sx={{ color: getRiskColor(marketRisk.risk_level) }}>
              {marketRisk.risk_level}
            </Typography>
            <Typography variant="subtitle1">
              Market Stress Probability: {marketRisk.probability}
            </Typography>
          </Card>
        </Grid>

        {/* Key Factors Card */}
        <Grid item xs={12} md={6}>
          <Card sx={{ p: 3 }}>
            <Box display="flex" alignItems="center" mb={2}>
              <TrendingUp sx={{ mr: 1 }} />
              <Typography variant="h6">Key Market Factors</Typography>
            </Box>
            <List>
              {data.key_factors.map((factor) => (
                <ListItem key={factor}>
                  <ListItemText
                    primary={factor}
                    secondary={`Current: ${data.current_readings[factor]}`}
                  />
                </ListItem>
              ))}
            </List>
          </Card>
        </Grid>

        {/* Recommendations Card */}
        <Grid item xs={12} md={6}>
          <Card sx={{ p: 3 }}>
            <Box display="flex" alignItems="center" mb={2}>
              <Assessment sx={{ mr: 1 }} />
              <Typography variant="h6">Recommended Actions</Typography>
            </Box>
            <List>
              {data.recommendations.map((rec, index) => (
                <ListItem key={index}>
                  <ListItemText primary={rec} />
                </ListItem>
              ))}
            </List>
          </Card>
        </Grid>

        {/* Detailed Analysis Card */}
        <Grid item xs={12} md={6}>
          <Card sx={{ p: 3 }}>
            <Box display="flex" alignItems="center" mb={2}>
              <Timeline sx={{ mr: 1 }} />
              <Typography variant="h6">Detailed Analysis</Typography>
            </Box>
            <Typography variant="body1" style={{ whiteSpace: 'pre-line' }}>
              {data.explanation}
            </Typography>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
};

export default MarketDashboard;
