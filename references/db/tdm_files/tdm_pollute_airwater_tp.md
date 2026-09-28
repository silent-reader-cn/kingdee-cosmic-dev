# 大气水污染信息暂存-tdm_pollute_airwater_tp

## 附件-附件表 t_tdm_airwater_attach_tp

- **表名称：** 附件-附件表
- **表名：** t_tdm_airwater_attach_tp

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
| 1 | pk_tdm_airwater_attach_tp |  | fpkid |
| 2 | idx_t_tdm_airwater_attach_tp |  | fid |

---

## 大气水污染信息暂存-多语言表 t_tdm_pollute_airwater_tp_l

- **表名称：** 大气水污染信息暂存-多语言表
- **表名：** t_tdm_pollute_airwater_tp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 排放口名称 | varchar | 50 |  | √ | ' ' | 排放口名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pollute_airwater_tp_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_pollute_airwater_tp_l |  | fpkid |

---

## 大气水污染信息暂存-主表 t_tdm_pollute_airwater_tp

- **表名称：** 大气水污染信息暂存-主表
- **表名：** t_tdm_pollute_airwater_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswrzl | 水污染种类 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 3 | ftestreport | 检测报告 | bpchar | 1 |  | √ | '0' | 检测报告 |
| 4 | fmonthend | 税款所属月份末 | timestamp | 0 |  |  | null | 税款所属月份末 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fhsz | 换算值 | numeric | 23 | 10 | √ | 0 | 换算值 |
| 7 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 8 | fqcpwxs | 排污系数 | numeric | 23 | 10 | √ | 0 | 排污系数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsdcbbs | 色度超标倍数 | numeric | 23 | 10 | √ | 0 | 色度超标倍数 |
| 11 | fenddate | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 12 | freductioncoefficient | 削减系数 | numeric | 23 | 10 | √ | 0 | 削减系数 |
| 13 | fsyxs | 适用系数 | varchar | 50 |  | √ | ' ' | 适用系数,枚举: cwxs :产污系数 pwxs :排污系数 |
| 14 | fsbbnum | 产排污系数的污染物名称 | varchar | 50 |  | √ | ' ' | 产排污系数的污染物名称 |
| 15 | fwrwdlz | 污染当量值 | numeric | 23 | 10 | √ | 0 | 污染当量值 |
| 16 | fnumber1 | 税源编码 | int8 | 64 |  | √ | 0 | [排污口基础信息 tdm_pollution_basedata](../tdm_files/tdm_pollution_basedata.md) |
| 17 | fexecstandard | 执行标准 | varchar | 50 |  | √ | ' ' | 执行标准 |
| 18 | fmonth | 税款所属月份 | timestamp | 0 |  |  | null | 税款所属月份 |
| 19 | fjsjcdw | 计税基数单位 | varchar | 50 |  | √ | ' ' | 计税基数单位,枚举: ton :吨 kg :千克 g :克 mg :毫克 |
| 20 | fcwxs | 产污系数 | numeric | 23 | 10 | √ | 0 | 产污系数 |
| 21 | fsbbbillno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 22 | fconstructionarea | 施工面积 | numeric | 23 | 10 | √ | 0 | 施工面积 |
| 23 | ftemplatefrom | 适用模板 | varchar | 50 |  | √ | ' ' | 适用模板,枚举: 1 :一类水、二类水、大气污染物-监测计算法 2 :一类水、二类水、大气污染物-产排污系数法 3 :一类水、二类水、大气污染物-物料衡算法 4 :PH值、色度、大肠菌群数、余氯量水污染物 5 :禽畜养殖业、小型企业和第三产业-抽样测算法 6 :施工排放扬尘-抽样测算法 |
| 24 | fwrwlb | 污染物类别 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 25 | fqcwrwdw | 污染物单位 | varchar | 50 |  | √ | ' ' | 污染物单位,枚举: ton :吨 tou :头 yu :羽 bed :床 |
| 26 | fscndz | 实测浓度值 | numeric | 23 | 10 | √ | 0 | 实测浓度值 |
| 27 | fwrwdls | 污染当量数 | numeric | 23 | 10 | √ | 0 | 污染当量数 |
| 28 | fname | 排放口名称 | varchar | 50 |  | √ | ' ' | 排放口名称 |
| 29 | fsbbbillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fbzndz | 标准浓度值 | numeric | 23 | 10 | √ | 0 | 标准浓度值 |
| 31 | fsbbdjstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态 |
| 32 | ftzl | 特征量 | numeric | 23 | 10 | √ | 0 | 特征量 |
| 33 | fdustgenerationcoefficie | 扬尘产生量系数 | numeric | 23 | 10 | √ | 0 | 扬尘产生量系数 |
| 34 | fstartdate | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 35 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fwrwdw | 污染物单位 | varchar | 50 |  | √ | ' ' | 污染物单位,枚举: ton :吨 kg :千克 g :克 mg :毫克 |
| 37 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板导入 |
| 38 | fnumber | 税源编码 | varchar | 30 |  | √ | ' ' | 税源编码 |
| 39 | fwrwmc | 污染物名称 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 40 | fpfknum | 排放口编号 | varchar | 50 |  | √ | ' ' | 排放口编号 |
| 41 | fwrwpfljsff | 污染物排放量计算方法 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 42 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |
| 43 | fyjndz | 月均浓度值 | numeric | 23 | 10 | √ | 0 | 月均浓度值 |
| 44 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 45 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 46 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 47 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 48 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 50 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fzgndz | 最高浓度值 | numeric | 23 | 10 | √ | 0 | 最高浓度值 |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fpfksszgswjg | 排放口所在地主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 55 | fjsjc | 计算基数 | numeric | 23 | 10 | √ | 0 | 计算基数 |
| 56 | fwrwname | 污染物名称 | varchar | 50 |  | √ | ' ' | 污染物名称 |
| 57 | fhygcpfwrwmc | 海洋工程排放污染物名称 | varchar | 50 |  | √ | ' ' | 海洋工程排放污染物名称 |
| 58 | fcharacteristiccoefficien | 特征系数 | numeric | 23 | 10 | √ | 0 | 特征系数 |
| 59 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 60 | fwrwpfl | 污染物排放量 | numeric | 23 | 10 | √ | 0 | 污染物排放量 |
| 61 | femissions | 废气（废水）排放量 | numeric | 23 | 10 | √ | 0 | 废气（废水）排放量 |
| 62 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 63 | fpwxs | 排污系数 | numeric | 23 | 10 | √ | 0 | 排污系数 |
| 64 | fjmxzdmhxmmc | 减免性质代码和项目名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 65 | fjmbl | 减免比例 | numeric | 23 | 10 | √ | 0 | 减免比例 |
| 66 | fndzbz | 浓度值比值 | numeric | 23 | 10 | √ | 0 | 浓度值比值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_pollute_airwater_tp |  | fid |
| 2 | idx_t_tdm_pollute_airwater_tp |  | fnumber |
