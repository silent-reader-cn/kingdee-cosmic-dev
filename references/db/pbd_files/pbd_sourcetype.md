# 寻源方式-pbd_sourcetype

## 寻源方式-多语言表 t_pds_extdata_l

- **表名称：** 寻源方式-多语言表
- **表名：** t_pds_extdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 1020 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extdata_l_fid |  | fid,flocaleid |
| 2 | pk_pds_extdata_l |  | fpkid |

---

## 寻源方式-主表 t_pds_extdata

- **表名称：** 寻源方式-主表
- **表名：** t_pds_extdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fishidden | fishidden | bpchar | 1 |  | √ | '0' |  |
| 3 | fgroupid | 资料类型 | int8 | 64 |  | √ | 0 | [寻源方式分组 pbd_sourcegroup](../pbd_files/pbd_sourcegroup.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fcheckitemid | fcheckitemid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmatchfield | fmatchfield | int4 | 32 |  | √ | 0 |  |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | foperatekey | 操作代码 | varchar | 50 |  | √ | ' ' | 操作代码 |
| 14 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 15 | fremark | fremark | varchar | 1000 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 20 | ffiletype | ffiletype | bpchar | 1 |  | √ | ' ' |  |
| 21 | fobjectid | fobjectid | varchar | 30 |  | √ | ' ' |  |
| 22 | fparamtype | 参数类型 | bpchar | 1 |  | √ | '0' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 |
| 23 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 24 | fisselloff | fisselloff | bpchar | 1 |  | √ | '0' |  |
| 25 | fdescription | fdescription | varchar | 510 |  | √ | ' ' |  |
| 26 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 27 | fparamvalue | 参数默认值 | varchar | 50 |  | √ | ' ' | 参数默认值 |
| 28 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extdata_fmasterid |  | fmasterid |
| 2 | idx_pds_extdata_fsrcbillid |  | fsrcbillid |
| 3 | idx_pds_extdata_fgroupid |  | fgroupid |
| 4 | idx_pds_extdata_number |  | fnumber |
| 5 | pk_pds_extdata |  | fid |
