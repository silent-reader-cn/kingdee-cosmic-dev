# 批量开票设置-bdm_issue_inv_setting

## 批量开票设置-主表 t_bdm_issue_inv_setttting

- **表名称：** 批量开票设置-主表
- **表名：** t_bdm_issue_inv_setttting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrcontinue | 开票失败是否继续 | bpchar | 1 |  | √ | ' ' | 开票失败是否继续 |
| 3 | fissueinvoiceorder | 开票顺序规则 | varchar | 50 |  | √ | ' ' | 开票顺序规则,枚举: |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | 企业管理 bdm_org |
| 5 | ffieldtolong | 字段超长处理规则 | varchar | 50 |  | √ | ' ' | 字段超长处理规则,枚举: 1 :超长提示 2 :超长截取 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_issue_inv_setttting |  | fid |
| 2 | idx_bdm_issue_inv_settting |  | forg |
