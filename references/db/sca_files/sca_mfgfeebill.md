# 制造费用归集_历史单据-sca_mfgfeebill

## 来源系统-多选基础资料表 t_sca_mfgfeecollc_srcsys

- **表名称：** 来源系统-多选基础资料表
- **表名：** t_sca_mfgfeecollc_srcsys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 60 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_mfgfeecollc_srcsys |  | fpkid |
| 2 | idex_sca_mfgfeecollc_srcsys |  | fid,fbasedataid |

---

## 制造费用归集_历史单据-多语言表 t_sca_mfgfeecollc_l

- **表名称：** 制造费用归集_历史单据-多语言表
- **表名：** t_sca_mfgfeecollc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_mfgfeecollc_l_pkey |  | fpkid |
| 2 | index_sca_mfgfeecollc_l |  | fid,flocaleid |

---

## 单据体-子表 t_sca_mfgfeecollcentry

- **表名称：** 单据体-子表
- **表名：** t_sca_mfgfeecollcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fvoucherentryid | 凭证分录id | varchar | 2000 |  | √ | ' ' | 凭证分录id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 7 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_mfgfeecollcentry_pkey |  | fentryid |
| 2 | index_sca_mfgfeecollcentry |  | fid,fsubelementid |

---

## 制造费用归集_历史单据-主表 t_sca_mfgfeecollc

- **表名称：** 制造费用归集_历史单据-主表
- **表名：** t_sca_mfgfeecollc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrcsysid | 来源系统 | varchar | 30 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 4 | fimpschid | 引入方案id | varchar | 2000 |  | √ | ' ' | 引入方案id |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalamount | 费用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用金额 |
| 7 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 8 | fappnum | fappnum | varchar | 100 |  | √ | ' ' |  |
| 9 | fsource | 来源(根据需求暂不显示) | varchar | 30 |  | √ | ' ' | 来源(根据需求暂不显示),枚举: MANUAL :手工新增 SYS :从业务系统引入 API :API引入 EXCEL :模板引入 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | frange | 费用分配范围 | varchar | 30 |  | √ | ' ' | 费用分配范围,枚举: A :不指定 B :指定受益成本中心 C :指定成本核算对象 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 14 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsrcbillid | 来源单据id | varchar | 2000 |  | √ | ' ' | 来源单据id |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fsrcbillnum | 来源单据号 | varchar | 2000 |  | √ | ' ' | 来源单据号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sca_mfgfeecollc |  | forgid,fcostcenterid |
| 2 | t_sca_mfgfeecollc_pkey |  | fid |
