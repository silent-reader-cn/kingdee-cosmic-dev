# 寻源方式-pbd_sourcetype

## 寻源方式-多语言表 t_pds_extdata_l

- **表名称：** 寻源方式-多语言表
- **表名：** t_pds_extdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

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
| 2 | fgroupid | 资料类型 | int8 | 64 |  | √ | 0 | 寻源方式分组 pbd_sourcegroup |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmatchfield | fmatchfield | int4 | 32 |  | √ | 0 |  |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | foperatekey | 操作代码 | varchar | 50 |  | √ | ' ' | 操作代码 |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fremark | fremark | varchar | 500 |  | √ | ' ' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fobjectid | fobjectid | varchar | 30 |  | √ | ' ' |  |
| 18 | fparamtype | 参数类型 | bpchar | 1 |  | √ | '0' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 |
| 19 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 20 | fisselloff | fisselloff | bpchar | 1 |  | √ | '0' |  |
| 21 | fdescription | fdescription | varchar | 510 |  | √ | ' ' |  |
| 22 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 23 | fparamvalue | 参数默认值 | varchar | 50 |  | √ | ' ' | 参数默认值 |
| 24 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extdata_fmasterid |  | fmasterid |
| 2 | idx_pds_extdata_fgroupid |  | fgroupid |
| 3 | idx_pds_extdata_number |  | fnumber |
| 4 | pk_pds_extdata |  | fid |
