# 电子签章-bos_ec_seal

## 电子签章-主表 t_bos_ec_seal

- **表名称：** 电子签章-主表
- **表名：** t_bos_ec_seal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsubjecttype | 主体类型 | varchar | 50 |  | √ | ' ' | 主体类型,枚举: 1 :合同主体 2 :签约主体 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fsealtypeid | 签章类型 | int8 | 64 |  | √ | 0 | [签章类型 bos_ec_sealtype](../base_files/bos_ec_sealtype.md) |
| 8 | fcompanyseal | 签章 | varchar | 255 |  | √ | ' ' | 签章 |
| 9 | fsubjectid | 主体ID | int8 | 64 |  | √ | 0 | 主体ID |
| 10 | fisdefault | 默认签章 | bpchar | 1 |  | √ | '0' | 默认签章 |
| 11 | fsignatureid | 签章ID | varchar | 50 |  | √ | ' ' | 签章ID |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bos_ec_seal |  | fid |
| 2 | idx_t_bos_ec_seal_sealtype |  | fsealtypeid,fsubjecttype,fsubjectid |
