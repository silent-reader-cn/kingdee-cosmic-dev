# 车辆税源信息-tdm_car_tax_fund_info

## 减免登记-子表 t_tdm_car_tax_fund_entry

- **表名称：** 减免登记-子表
- **表名：** t_tdm_car_tax_fund_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 3 | fratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 6 | fend | 减税终止时间 | timestamp | 0 |  |  | null | 减税终止时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_car_tax_fund_entry |  | fentryid |
| 2 | idx_tdm_car_tax_fund_entry_fk |  | fid |

---

## 车辆税源信息-主表 t_tdm_car_tax_fund_info

- **表名称：** 车辆税源信息-主表
- **表名：** t_tdm_car_tax_fund_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fvin | 车辆识别号（车架号码） | varchar | 50 |  | √ | ' ' | 车辆识别号（车架号码） |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurbweight | 整备质量 | int8 | 64 |  | √ | 0 | 整备质量 |
| 6 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 7 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 8 | fapprovedpasseng | 核定载客 | int8 | 64 |  | √ | 0 | 核定载客 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplatenumber | 车牌号码 | varchar | 50 |  | √ | ' ' | 车牌号码 |
| 11 | fsbqx | 申报月份（年度终了前） | varchar | 50 |  | √ | '12' | 申报月份（年度终了前）,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fzbzl | 整备质量（吨） | numeric | 23 | 10 | √ | 0 | 整备质量（吨） |
| 17 | fvehicleregdate | 车辆发票日期或注册登记日期 | timestamp | 0 |  |  | null | 车辆发票日期或注册登记日期 |
| 18 | fwithheld | 是否代扣代缴 | bpchar | 1 |  | √ | ' ' | 是否代扣代缴 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ffueltype | 燃料种类 | varchar | 50 |  | √ | ' ' | 燃料种类 |
| 21 | ftaxauthority | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbrandmodel | 车辆品牌 | varchar | 50 |  | √ | ' ' | 车辆品牌 |
| 24 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 25 | fcartype | 车辆型号 | varchar | 50 |  | √ | ' ' | 车辆型号 |
| 26 | fpail | 排气量（升） | numeric | 23 | 10 | √ | 0 | 排气量（升） |
| 27 | fdatefield | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 28 | fengineno | 发动机号 | varchar | 50 |  | √ | ' ' | 发动机号 |
| 29 | fitemcollection | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型,枚举: 1 :1.0升（含）以下的乘用车 2 :1.0升以上至1.6升（含）的乘用车 3 :1.6升以上至2.0升（含）的乘用车 4 :2.0升以上至2.5升（含）的乘用车 5 :2.5升以上至3.0升（含）的乘用车 6 :3.0升以上至4.0升（含）的乘用车 7 :4.0升以上的乘用车 8 :核定载客人数20人以下客车 9 :核定载客人数20人（含）以上客车 10 :货车 11 :挂车 12 :专用作业车 13 :轮式专用机械车 14 :摩托车 |
| 30 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 31 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 32 | fnumber | 车辆编号 | varchar | 30 |  | √ | ' ' | 车辆编号 |
| 33 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 34 | fusecharacter | 使用性质 | varchar | 50 |  | √ | ' ' | 使用性质 |
| 35 | fdisplacement | 排量-废弃 | int8 | 64 |  | √ | 0 | 排量-废弃 |
| 36 | fdatatype | 数据来源 | varchar | 50 |  | √ | '1' | 数据来源,枚举: 1 :手工新增 2 :税局下载 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_car_tax_fund_info |  | fnumber |
| 2 | t_tdm_car_tax_fund_info_pkey |  | fid |

---

## 车辆税源信息-多语言表 t_tdm_car_tax_fund_info_l

- **表名称：** 车辆税源信息-多语言表
- **表名：** t_tdm_car_tax_fund_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_car_tax_fund_info_l_0 |  | fid,flocaleid |
| 2 | t_tdm_car_tax_fund_info_l_pkey |  | fpkid |

---

## 资产编码-多选基础资料表 t_tdm_car_asset

- **表名称：** 资产编码-多选基础资料表
- **表名：** t_tdm_car_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产清单 tdm_asset_data](../tdm_files/tdm_asset_data.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_car_asset |  | fpkid |
| 2 | idx_tdm_car_asset_fk |  | fid |
