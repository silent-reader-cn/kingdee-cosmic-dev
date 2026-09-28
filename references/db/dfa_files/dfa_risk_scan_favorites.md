# 风险扫描收藏夹-dfa_risk_scan_favorites

## 风险扫描收藏夹-主表 t_dfa_risk_scan_favorites

- **表名称：** 风险扫描收藏夹-主表
- **表名：** t_dfa_risk_scan_favorites

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstockcode | 上市公司股票代码 | varchar | 50 |  | √ | ' ' | 上市公司股票代码 |
| 3 | fuser | 用户ID | varchar | 50 |  | √ | ' ' | 用户ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_user |  | fuser |
| 2 | pk_t_dfa_risk_scan_favorites |  | fid |
