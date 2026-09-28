# 组织交接关系-bos_org_handover

## 组织交接关系-主表 t_org_handover

- **表名称：** 组织交接关系-主表
- **表名：** t_org_handover

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fhandoverorgid | 交接组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbizid | 职能类型 | int8 | 64 |  | √ | 0 | 组织职能类型 bos_org_biz |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_handover |  | fid |
| 2 | idx_t_org_handover |  | fbizid,forgid,fhandoverorgid |
