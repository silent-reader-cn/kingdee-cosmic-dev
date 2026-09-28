# 基础资料录入（废弃）-ipop_initbasedata

## 基础资料录入（废弃）-主表 t_ipop_initbasedata

- **表名称：** 基础资料录入（废弃）-主表
- **表名：** t_ipop_initbasedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeid | 类型id | int8 | 64 |  | √ | 0 | [基础资料录入类型（废弃） ipop_initbasedatatype](../ipop_files/ipop_initbasedatatype.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fappnumber | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodulecode | 模块编码 | varchar | 50 |  | √ | ' ' | 模块编码 |
| 9 | fmarkfinish | 标记完成 | bpchar | 1 |  | √ | ' ' | 标记完成 |
| 10 | fformid | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_initbasedata_app |  | fappnumber |
| 2 | idx_ipop_initbasedata_fid |  | fformid |
| 3 | idx_ipop_initbasedata_mid |  | fmodulecode |
| 4 | idx_ipop_initbasedata_tid |  | ftypeid |
| 5 | idx_ipop_initbasedata_org |  | forgid |
| 6 | pk_t_ipop_initbasedata |  | fid |
