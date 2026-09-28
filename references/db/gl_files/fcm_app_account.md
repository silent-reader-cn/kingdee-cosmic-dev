# 应用账簿编码-fcm_app_account

## 应用账簿编码-主表 t_fcm_app_account

- **表名称：** 应用账簿编码-主表
- **表名：** t_fcm_app_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodentityname | 当前期间查询实体名称 | varchar | 100 |  | √ | ' ' | 当前期间查询实体名称 |
| 3 | fperiodidproperty | 当前期间ID属性路径 | varchar | 100 |  | √ | ' ' | 当前期间ID属性路径 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | faccounttypename | 账簿类型名称 | varchar | 50 |  | √ | ' ' | 账簿类型名称 |
| 7 | ffilterstr | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fsearchfield | 查询字段 | varchar | 2000 |  | √ | ' ' | 查询字段 |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fperiodfilterexpr | 当前期间过滤表达式 | varchar | 400 |  | √ | ' ' | 当前期间过滤表达式 |
| 12 | faccountentity | 应用账簿 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | faccounttype | 账簿类型字段 | varchar | 30 |  | √ | ' ' | 账簿类型字段 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_app_account |  | fid |
| 2 | idx_fcm_app_acoount |  | fbizappid |
