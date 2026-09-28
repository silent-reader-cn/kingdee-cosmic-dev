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
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftaxproject | 税务项目编码 | int8 | 64 |  | √ | 0 | [税务项目信息 bastax_taxproject](../bastax_files/bastax_taxproject.md) |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsstdzzsfq | 所属土地增值税分期 | varchar | 50 |  | √ | ' ' | 所属土地增值税分期,枚举: 01 :一期 02 :二期 03 :三期 04 :四期 05 :五期 06 :六期 07 :七期 08 :八期 09 :九期 10 :十期 |
| 8 | flocation | 项目所在地 | varchar | 50 |  | √ | ' ' | 项目所在地 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | funitbudget | 单位预算成本 | numeric | 23 | 10 | √ | 0 | 单位预算成本 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 项目建设结束时间 | timestamp | 0 |  |  | null | 项目建设结束时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftotalbuildingarea | 开发建筑总面积 | numeric | 23 | 10 | √ | 0 | 开发建筑总面积 |
| 16 | fswqsytfl | 税务业态分类方法 | varchar | 50 |  | √ | ' ' | 税务业态分类方法,枚举: 0 :二分法 1 :三分法 |
| 17 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 18 | fname | 项目名称 | varchar | 400 |  | √ | ' ' | 项目名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ftotallandarea | 开发土地总面积 | numeric | 23 | 10 | √ | 0 | 开发土地总面积 |
| 21 | ftdxsytsftscl | 特定业态是否计税 | bpchar | 1 |  | √ | '0' | 特定业态是否计税 |
| 22 | ftaxauthority | 项目主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 23 | fissimplecalculation | 是否适用简化计算方法 | bpchar | 1 |  | √ | '0' | 是否适用简化计算方法 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fisallowdeductprice | 预缴时是否考虑当期允许扣除的土地价款 | bpchar | 1 |  | √ | '0' | 预缴时是否考虑当期允许扣除的土地价款 |
| 26 | fapplyrate | 适用税率/征收率 | varchar | 50 |  | √ | ' ' | 适用税率/征收率,枚举: nine :9% five :5% |
| 27 | fpaymentdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月度 season :季度 |
| 28 | ftotalbudget | 总预算成本 | numeric | 23 | 10 | √ | 0 | 总预算成本 |
| 29 | fstartdate | 项目建设开始时间 | timestamp | 0 |  |  | null | 项目建设开始时间 |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 项目编码 | varchar | 30 |  | √ | ' ' | 项目编码 |
| 32 | fphase | 项目所处阶段 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 33 | flevymethod | 增值税征收方式 | varchar | 50 |  | √ | ' ' | 增值税征收方式,枚举: general :一般计税 simple :简易计税 |

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

## 预征计征依据维护列表-子表 t_tdm_tdzzs_xm_yzjzyj

- **表名称：** 预征计征依据维护列表-子表
- **表名：** t_tdm_tdzzs_xm_yzjzyj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyxqq | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 3 | fyzjzyjqdff | 预征计征依据确定方法 | varchar | 50 |  | √ | ' ' | 预征计征依据确定方法,枚举: jzzs :预收款减预缴增值税 jxxs :预收款减销项税 |
| 4 | fyxqz | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tdzzs_xm_yzjzyj |  | fentryid |
| 2 | idx_tdm_tdzzs_xm_yzjzyj_fk |  | fid |

---

## 预缴内容-子表 t_tdm_tdzzs_prepay_info

- **表名称：** 预缴内容-子表
- **表名：** t_tdm_tdzzs_prepay_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbuildingtype | 税务业态 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fprelevyrate | 预征率 | numeric | 23 | 10 | √ | 0 | 预征率 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexpirationend | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 6 | fsubbuildingtype | 房产类型子目 | int8 | 64 |  | √ | 0 | [房产类型子目 tcret_tdzzs_fclxzm](../tcret_files/tcret_tdzzs_fclxzm.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexpirationstart | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |

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

## 房间归集-子表 t_tdm_tdzzs_fjgj

- **表名称：** 房间归集-子表
- **表名：** t_tdm_tdzzs_fjgj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmj | 面积 | numeric | 23 | 10 | √ | 0 | 面积 |
| 3 | fsftdyt | 是否计税 | varchar | 50 |  | √ | ' ' | 是否计税,枚举: no :否 yes :是 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fxsyt | 销售业态 | int8 | 64 |  | √ | 0 | [销售业态 bastax_saleformat](../bastax_files/bastax_saleformat.md) |
| 6 | fdj | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 7 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 8 | fzj | 总价 | numeric | 23 | 10 | √ | 0 | 总价 |
| 9 | fkszc | 可售/自持 | varchar | 50 |  | √ | ' ' | 可售/自持,枚举: 0 :可售 1 :自持 |
| 10 | ffjly | 房间来源 | varchar | 50 |  | √ | ' ' | 房间来源,枚举: csfa :测算方案 sgcj :手工创建 |
| 11 | froombasedata | 房间编码 | int8 | 64 |  | √ | 0 | [房间基础信息 bastax_room](../bastax_files/bastax_room.md) |
| 12 | fsbjd | 申报阶段 | varchar | 50 |  | √ | ' ' | 申报阶段,枚举: wsb :未申报 yyzsb :已预征申报 yqssb :已清算申报 ywpsb :已尾盘申报 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fqyrq | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tdzzs_fjgj_fk |  | fid |
| 2 | pk_tdm_tdzzs_fjgj |  | fentryid |

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
