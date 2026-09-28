# 刷新bom操作记录-cad_refreshbomrecord

## 刷新bom操作记录-主表 t_cad_refreshbomrecord

- **表名称：** 刷新bom操作记录-主表
- **表名：** t_cad_refreshbomrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 4 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | frefreshnewmat | 仅刷新新增物料 | bpchar | 1 |  | √ | '0' | 仅刷新新增物料 |
| 6 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_refreshbomrecord |  | fid |
| 2 | idx_t_cad_refreshbomrecord |  | fcalorgid,fuserid |
