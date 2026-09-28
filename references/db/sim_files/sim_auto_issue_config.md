# 自动开票单据-sim_auto_issue_config

## 自动开票单据-主表 t_sim_auto_issue_config

- **表名称：** 自动开票单据-主表
- **表名：** t_sim_auto_issue_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fuseorg | 适用组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | freason | 重开原因 | varchar | 2500 |  | √ | ' ' | 重开原因,枚举: |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_auto_issue_config |  | fid |
| 2 | idx_sim_auto_issue_config |  | fuseorg |
