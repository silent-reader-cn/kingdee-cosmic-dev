# 固体废物信息采集表-tdm_solid_waste_info

## 固体废物信息采集表-主表 t_tdm_solid_waste_info

- **表名称：** 固体废物信息采集表-主表
- **表名：** t_tdm_solid_waste_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftestreport | 检测报告 | varchar | 1 |  | √ | ' ' | 检测报告 |
| 3 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 4 | fbydtfwcsl | 本月固体废物产生量（吨） | numeric | 23 | 10 | √ | 0 | 本月固体废物产生量（吨） |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 7 | fendmonth | 月末 | timestamp | 0 |  |  | null | 月末 |
| 8 | fpfkname | 排放口名称 | varchar | 50 |  | √ | ' ' | 排放口名称 |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 10 | fwrwzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fdeclarestatus | 申报状态（废弃） | varchar | 50 |  | √ | ' ' | 申报状态（废弃）,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 14 | fenddate | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fpollutiondataid | 税源编码 | int8 | 64 |  | √ | 0 | [排污口基础信息 tcret_pollution_basedata](../tcret_files/tcret_pollution_basedata.md) |
| 18 | fmonth | 税款所属月份 | timestamp | 0 |  |  | null | 税款所属月份 |
| 19 | ftaxdeduction | 减免性质代码和项目名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 20 | fsbbbillno | 申报表编号（废弃） | varchar | 50 |  | √ | ' ' | 申报表编号（废弃） |
| 21 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 22 | fwrwlb | 污染物类别 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fsbbbillstatus | 申报表单据状态（废弃） | varchar | 50 |  | √ | ' ' | 申报表单据状态（废弃）,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fpfksszgswjg | 排放口所属主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 29 | fqtgtfw | 其他固体废物 | varchar | 50 |  | √ | ' ' | 其他固体废物 |
| 30 | fbygtfwzhlyl | 本月固体废物综合利用量（吨） | numeric | 23 | 10 | √ | 0 | 本月固体废物综合利用量（吨） |
| 31 | fpfknumber | 排放口编号 | varchar | 50 |  | √ | ' ' | 排放口编号 |
| 32 | fwrwname | 污染物名称 | varchar | 50 |  | √ | ' ' | 污染物名称 |
| 33 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 34 | fwrwpfl | 污染物排放量（吨） | numeric | 23 | 10 | √ | 0 | 污染物排放量（吨） |
| 35 | fccqk | 贮存情况 | varchar | 50 |  | √ | ' ' | 贮存情况 |
| 36 | fzhlyqk | 综合利用情况 | varchar | 50 |  | √ | ' ' | 综合利用情况,枚举: 1 :金属材料回收 2 :非金属材料回收 3 :能量回收 4 :其他方式 |
| 37 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 38 | fstartdate | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 39 | fbygtfwczl | 本月固体废物处置量（吨） | numeric | 23 | 10 | √ | 0 | 本月固体废物处置量（吨） |
| 40 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 41 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板导入 |
| 43 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 44 | fczqk | 处置情况 | varchar | 50 |  | √ | ' ' | 处置情况 |
| 45 | fwrwmc | 污染物名称 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_hbs_bizdefen_tree |
| 46 | fbygtfwccl | 本月固体废物贮存量（吨） | numeric | 23 | 10 | √ | 0 | 本月固体废物贮存量（吨） |
| 47 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_solid_waste_info_1 |  | fnumber |
| 2 | pk_tdm_solid_waste_info |  | fid |

---

## 附件-附件表 t_tdm_solidwaste_attach

- **表名称：** 附件-附件表
- **表名：** t_tdm_solidwaste_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_solidwaste_attach |  | fpkid |
| 2 | idx_t_tdm_solidwaste_attach |  | fid |

---

## 固体废物信息采集表-多语言表 t_tdm_solid_waste_info_l

- **表名称：** 固体废物信息采集表-多语言表
- **表名：** t_tdm_solid_waste_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_solid_waste_info_l |  | fpkid |
| 2 | idx_tdm_solid_waste_info_l_0 |  | fid,flocaleid |
