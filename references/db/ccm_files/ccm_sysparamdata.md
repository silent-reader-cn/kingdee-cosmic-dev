# 信用管理后台参数-ccm_sysparamdata

## 信用管理后台参数-主表 t_ccm_sysparamdata

- **表名称：** 信用管理后台参数-主表
- **表名：** t_ccm_sysparamdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 100 |  | √ | ' ' | 参数值 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fparamkey | 参数标识 | varchar | 50 |  | √ | ' ' | 参数标识,枚举: supportmultibill :信用控制方案支持同一业务单据多个单据策略（默认值：false） recalbatchbillcount :信用重算分批计算每一批的记录数（默认值：200000） maxrptquerycount :信用报表数据来源最大记录数（默认值：100000） maxentrycount :动态表单单据体最大显示记录数（默认值：10000） getarchivemaxcount :API查询最大返回档案数（默认值：2000） maxnetctrlretrycount :信用更新网控最大重试次数（默认值：10） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_sysparamdata |  | fid |
| 2 | idx_ccm_sysparamdata |  | fparamkey |
