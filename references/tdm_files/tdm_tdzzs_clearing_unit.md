# 土地增值税项目-tdm_tdzzs_clearing_unit

## 土地增值税项目-主表 t_tdm_tdzzs_clearing_unit

- **表名称：** 土地增值税项目-主表
- **表名：** t_tdm_tdzzs_clearing_unit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 项目详细地址 | varchar | 550 |  | √ | ' ' | 项目详细地址 |
| 3 | ftransfercontractname | 房地产转让合同名称 | varchar | 50 |  | √ | ' ' | 房地产转让合同名称 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftaxproject | 税务项目编码 | int8 | 64 |  | √ | 0 | 税务项目信息 bastax_taxproject |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | flocation | 项目所在地 | varchar | 50 |  | √ | ' ' | 项目所在地 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | funitbudget | 单位预算成本 | numeric | 23 | 10 | √ | 0 | 单位预算成本 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 项目建设结束时间 | timestamp | 0 |  |  | null | 项目建设结束时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftotalbuildingarea | 开发建筑总面积 | numeric | 23 | 10 | √ | 0 | 开发建筑总面积 |
| 15 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 16 | fname | 项目名称 | varchar | 400 |  | √ | ' ' | 项目名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftotallandarea | 开发土地总面积 | numeric | 23 | 10 | √ | 0 | 开发土地总面积 |
| 19 | ftaxauthority | 项目主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 20 | fissimplecalculation | 是否适用简化计算方法 | bpchar | 1 |  | √ | '0' | 是否适用简化计算方法 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fisallowdeductprice | 预缴时是否考虑当期允许扣除的土地价款 | bpchar | 1 |  | √ | '0' | 预缴时是否考虑当期允许扣除的土地价款 |
| 23 | fapplyrate | 适用税率/征收率 | varchar | 50 |  | √ | ' ' | 适用税率/征收率,枚举: nine :9% five :5% |
| 24 | fpaymentdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月度 season :季度 |
| 25 | ftotalbudget | 总预算成本 | numeric | 23 | 10 | √ | 0 | 总预算成本 |
| 26 | fstartdate | 项目建设开始时间 | timestamp | 0 |  |  | null | 项目建设开始时间 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 项目编码 | varchar | 30 |  | √ | ' ' | 项目编码 |
| 29 | fphase | 项目所处阶段 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 30 | flevymethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: general :一般计税 simple :简易计税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_clearing_1 |  | forgid,ftaxorg,ftaxproject |
| 2 | pk_tdm_tdzzs_clearing_unit |  | fid |

---

## 土地内容-子表 t_tdm_tdzzs_land_info

- **表名称：** 土地内容-子表
- **表名：** t_tdm_tdzzs_land_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flandsourceinfo | 土地税源信息 | varchar | 50 |  | √ | ' ' | 土地税源信息 |
| 3 | flandcontractno | 土地使用权受让（行政划拨）合同号 | varchar | 50 |  | √ | ' ' | 土地使用权受让（行政划拨）合同号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flanddate | 受让（行政划拨）时间 | timestamp | 0 |  |  | null | 受让（行政划拨）时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_land_info_1 |  | fid |
| 2 | pk_tdm_tdzzs_land_info |  | fentryid |

---

## 预缴内容-子表 t_tdm_tdzzs_prepay_info

- **表名称：** 预缴内容-子表
- **表名：** t_tdm_tdzzs_prepay_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbuildingtype | 房产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fprelevyrate | 预征率 | numeric | 23 | 10 | √ | 0 | 预征率 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsubbuildingtype | 房产类型子目 | int8 | 64 |  | √ | 0 | 房产类型子目 tcret_tdzzs_fclxzm |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tdzzs_prepay_info |  | fentryid |
| 2 | idx_t_tdm_tdzzs_prepay_info_1 |  | fid |

---

## 转让内容-子表 t_tdm_tdzzs_transfer_info

- **表名称：** 转让内容-子表
- **表名：** t_tdm_tdzzs_transfer_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flandtransferarea | 本次转让土地面积 | numeric | 23 | 10 | √ | 0 | 本次转让土地面积 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | ftransferremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fbuildingtransferarea | 本次转让建筑面积 | numeric | 23 | 10 | √ | 0 | 本次转让建筑面积 |
| 5 | ftransfercontractdate | 转让合同签订日期 | timestamp | 0 |  |  | null | 转让合同签订日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_transfer_in_1 |  | fid |
| 2 | pk_tdm_tdzzs_transfer_info |  | fentryid |

---

## 土地增值税项目-多语言表 t_tdm_tdzzs_clearing_unit_l

- **表名称：** 土地增值税项目-多语言表
- **表名：** t_tdm_tdzzs_clearing_unit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 400 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tdzzs_clearing_unit_l |  | fpkid |
| 2 | idx_tdm_tdzzs_clearing_uni_l_0 |  | fid,flocaleid |
