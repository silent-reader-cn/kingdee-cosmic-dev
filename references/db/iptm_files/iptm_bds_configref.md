# 业务数据统计配置关系表-iptm_bds_configref

## 业务数据统计配置关系表-主表 t_iptm_bds_configref

- **表名称：** 业务数据统计配置关系表-主表
- **表名：** t_iptm_bds_configref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmastercfgid | 主业务单据配置 | int8 | 64 |  | √ | 0 | [业务数据统计配置表 iptm_bds_config](../iptm_files/iptm_bds_config.md) |
| 3 | frelationcfgid | 关联业务单据配置 | int8 | 64 |  | √ | 0 | [业务数据统计配置表 iptm_bds_config](../iptm_files/iptm_bds_config.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_bds_configref |  | fid |
| 2 | idx_iptm_bds_configref_mcfgid |  | fmastercfgid |
