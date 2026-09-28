# 制造费用归集_历史单据-aca_mfgfeebill

## 单据体-子表 t_aca_mfgfeecollcentry

- **表名称：** 单据体-子表
- **表名：** t_aca_mfgfeecollcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fvoucherentryid | 凭证分录id | int8 | 64 |  | √ | 0 | 凭证分录id |
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
| 1 | pk_t_aca_mfgfeecollcentry |  | fentryid |
| 2 | idx_aca_mfgfeecollcentry |  | fid,fsubelementid |

---

## 制造费用归集_历史单据-多语言表 t_aca_mfgfeecollc_l

- **表名称：** 制造费用归集_历史单据-多语言表
- **表名：** t_aca_mfgfeecollc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_mfgfeecollc_l |  | fid,flocaleid |
| 2 | pk_t_aca_mfgfeecollc_l |  | fpkid |

---

## 制造费用归集_历史单据-主表 t_aca_mfgfeecollc

- **表名称：** 制造费用归集_历史单据-主表
- **表名：** t_aca_mfgfeecollc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrcsysid | 来源系统 | varchar | 30 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 4 | fimpschid | 引入方案id | int8 | 64 |  | √ | 0 | 引入方案id |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalamount | 费用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用金额 |
| 7 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 8 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 9 | fsource | 来源(根据需求暂不显示) | varchar | 30 |  | √ | ' ' | 来源(根据需求暂不显示),枚举: MANUAL :手工新增 SYS :从业务系统引入 API :API引入 EXCEL :模板引入 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fsrcbillnum | 来源单据号 | varchar | 60 |  | √ | ' ' | 来源单据号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_mfgfeecollc |  | fid |
| 2 | idx_aca_mfgfeecollc |  | forgid,fcostcenterid |
