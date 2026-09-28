# 用户数据规则的引用属性规则-perm_userdatarule_prop

## 用户数据规则的引用属性规则-主表 t_perm_userdatarule_prop

- **表名称：** 用户数据规则的引用属性规则-主表
- **表名：** t_perm_userdatarule_prop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdataruleid | 数据规则方案 | int8 | 64 |  | √ | 0 | [数据规则方案 perm_datarule](../base_files/perm_datarule.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisincludesub | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 8 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpropentnum | 属性对应业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdimtype | 隔离维度类型 | varchar | 36 |  | √ | ' ' | 隔离维度类型,枚举: bos_org :业务单元 |
| 13 | fpropkey | 属性标识 | varchar | 60 |  | √ | ' ' | 属性标识 |
| 14 | fdimid | 隔离维度对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_usrdr_prop_qry |  | fuserid,fappid,fentitynum,fpropkey |
| 2 | pk_t_perm_userdatarule_prop |  | fid |
