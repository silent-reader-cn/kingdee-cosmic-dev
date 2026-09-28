# 开证记录查询-lc_onlineresult

## 开证记录查询-分表 t_lc_onlineresult_e

- **表名称：** 开证记录查询-分表
- **表名：** t_lc_onlineresult_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgasdescription_tag | 货物/劳务描述_详情 | text | 0 |  |  | null | 货物/劳务描述_详情 |
| 3 | fdraweeaddress | 受票行地址 | varchar | 255 |  | √ | ' ' | 受票行地址 |
| 4 | fissuingbankbic | 开证行BIC | varchar | 50 |  | √ | ' ' | 开证行BIC |
| 5 | faddclause_tag | 附加条款_详情 | text | 0 |  |  | null | 附加条款_详情 |
| 6 | fstartair | 装运港/始发机场 | varchar | 255 |  | √ | ' ' | 装运港/始发机场 |
| 7 | ftermini | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 8 | faddclause | 附加条款 | varchar | 255 |  | √ | ' ' | 附加条款 |
| 9 | fdraftproportion | 汇票与发票金额的比例 | varchar | 50 |  | √ | ' ' | 汇票与发票金额的比例 |
| 10 | fspotarriveamt | 即期已到单金额 | numeric | 19 | 6 | √ | 0 | 即期已到单金额 |
| 11 | fdocclause_tag | 单据条款_详情 | text | 0 |  |  | null | 单据条款_详情 |
| 12 | fmixdraftinvproportion | 混合汇票与发票金额的比例 | varchar | 50 |  | √ | ' ' | 混合汇票与发票金额的比例 |
| 13 | fpaydays | 付款天数 | varchar | 50 |  | √ | ' ' | 付款天数 |
| 14 | fmixtenordays | 混合付款天数 | varchar | 50 |  | √ | ' ' | 混合付款天数 |
| 15 | fforwardarriveamt | 远期已到单金额 | numeric | 19 | 6 | √ | 0 | 远期已到单金额 |
| 16 | fabtimes | 到单次数 | varchar | 50 |  | √ | ' ' | 到单次数 |
| 17 | fcreditstatus | 当前信用证状态 | varchar | 50 |  | √ | ' ' | 当前信用证状态 |
| 18 | fistranship | 转运 | varchar | 50 |  | √ | ' ' | 转运 |
| 19 | fispartship | 分批 | varchar | 50 |  | √ | ' ' | 分批 |
| 20 | fpayamtdone | 已付款金额 | numeric | 19 | 6 | √ | 0 | 已付款金额 |
| 21 | flcbillno | 开证单据编号 | varchar | 80 |  | √ | ' ' | 开证单据编号 |
| 22 | flastshipdate | 最迟装运期 | varchar | 50 |  | √ | ' ' | 最迟装运期 |
| 23 | fdraweecnapscode | 受票行BIC | varchar | 50 |  | √ | ' ' | 受票行BIC |
| 24 | fterminiair | 卸货港/目的地机场 | varchar | 255 |  | √ | ' ' | 卸货港/目的地机场 |
| 25 | fshipdate | 装运期 | varchar | 255 |  | √ | ' ' | 装运期 |
| 26 | fpresentperiod | 交单期限 | varchar | 255 |  | √ | ' ' | 交单期限 |
| 27 | fpaytype | 付款类型 | varchar | 50 |  | √ | ' ' | 付款类型,枚举: 1 :AT SIGHT 2 :DAYS AFTER SIGHT 3 :DAYS AFTER B/L DATE 4 :DAYS FROM B/L DATE 5 :DAYS FROM INVOICE DATE 6 :DAYS AFTER SHIPPING DATE 7 :DAYS FROM SHIPPING DATE 8 :Others |
| 28 | fserialnumber | 客户流水号 | varchar | 50 |  | √ | ' ' | 客户流水号 |
| 29 | fexplain_tag | 期限描述_详情 | text | 0 |  |  | null | 期限描述_详情 |
| 30 | fmixdraftinvamt | 混合汇票与发票金额 | numeric | 19 | 6 | √ | 0 | 混合汇票与发票金额 |
| 31 | fdraftamt | 汇票与发票金额 | numeric | 19 | 6 | √ | 0 | 汇票与发票金额 |
| 32 | fotherbankinstruction | 他行指示内容 | varchar | 255 |  | √ | ' ' | 他行指示内容 |
| 33 | fdocclause | 单据条款 | varchar | 255 |  | √ | ' ' | 单据条款 |
| 34 | fgasdescription | 货物/劳务描述 | varchar | 255 |  | √ | ' ' | 货物/劳务描述 |
| 35 | fotherbankinstruction_tag | 他行指示内容_详情 | text | 0 |  |  | null | 他行指示内容_详情 |
| 36 | fmixtenortype | 混合付款类型 | varchar | 50 |  | √ | ' ' | 混合付款类型,枚举: 1 :AT SIGHT 2 :DAYS AFTER SIGHT 3 :DAYS AFTER B/L DATE 4 :DAYS FROM B/L DATE 5 :DAYS FROM INVOICE DATE 6 :DAYS AFTER SHIPPING DATE 7 :DAYS FROM SHIPPING DATE 8 :Others |
| 37 | fpresentday | 交单天数 | varchar | 50 |  | √ | ' ' | 交单天数 |
| 38 | fdeliveryport | 收货地 | varchar | 255 |  | √ | ' ' | 收货地 |
| 39 | fexplain | 期限描述 | varchar | 255 |  | √ | ' ' | 期限描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_onlineresult_e |  | fid |
| 2 | idx_onlineresult_estatus |  | fcreditstatus |

---

## 开证记录查询-反写记录表 t_lc_onlineresult_wb

- **表名称：** 开证记录查询-反写记录表
- **表名：** t_lc_onlineresult_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_onlineresult_wb |  | fentryid |
| 2 | idx_lc_onlineresult_wb_fk |  | fid |

---

## 开证记录查询-主表 t_lc_onlineresult

- **表名称：** 开证记录查询-主表
- **表名：** t_lc_onlineresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadvicnapscode | 通知行BIC | varchar | 50 |  | √ | ' ' | 通知行BIC |
| 3 | favwtbankbic | 指定有关银行BIC | varchar | 50 |  | √ | ' ' | 指定有关银行BIC |
| 4 | fcreditmode | 开证方式 | varchar | 50 |  | √ | ' ' | 开证方式,枚举: 1 :全电SWIFT 2 :简电SWIFT+证实书 3 :信开Mail |
| 5 | fcounteraddress | 受益人名称地址 | varchar | 255 |  | √ | ' ' | 受益人名称地址 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmoreproportion | 溢装比例 | varchar | 50 |  | √ | ' ' | 溢装比例 |
| 8 | fcreditno | 信用证号码 | varchar | 50 |  | √ | ' ' | 信用证号码 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 10 | favwtbanknmadd | 指定有关银行地址 | varchar | 255 |  | √ | ' ' | 指定有关银行地址 |
| 11 | fforwardcnapscode | 转通知行BIC | varchar | 50 |  | √ | ' ' | 转通知行BIC |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | flessproportion | 短装比例 | varchar | 50 |  | √ | ' ' | 短装比例 |
| 14 | fcredittype | 信用证类型 | varchar | 50 |  | √ | ' ' | 信用证类型,枚举: 1 :即期信用证 2 :远期信用证 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | facceptorcnapscode | 保兑行BIC | varchar | 50 |  | √ | ' ' | 保兑行BIC |
| 17 | fapplicantname | 申请人名称 | varchar | 255 |  | √ | ' ' | 申请人名称 |
| 18 | fconinstructions | 保兑指示 | varchar | 50 |  | √ | ' ' | 保兑指示,枚举: 1 :CONFIRM 2 :MAY ADD 3 :WITHOUT |
| 19 | fdraftcustflg | 需要汇票 | varchar | 50 |  | √ | ' ' | 需要汇票 |
| 20 | fcostbear | 手续费承担方 | varchar | 255 |  | √ | ' ' | 手续费承担方 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fcountername | 受益人名称 | varchar | 255 |  | √ | ' ' | 受益人名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdueaddress | 到期地点 | varchar | 255 |  | √ | ' ' | 到期地点 |
| 25 | favwtbank | 指定有关银行 | varchar | 50 |  | √ | ' ' | 指定有关银行,枚举: 1 :ANY BANK 2 :Advising Bank 3 :Issuing Bank 4 :Other Bank |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcharcurrency | 手续费扣费账号币种 | varchar | 50 |  | √ | ' ' | 手续费扣费账号币种 |
| 28 | facceptoraddress | 保兑行地址 | varchar | 255 |  | √ | ' ' | 保兑行地址 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fadviaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 31 | fcurrency | 信用证币种 | varchar | 50 |  | √ | ' ' | 信用证币种 |
| 32 | fcreditform | 信用证形式 | varchar | 50 |  | √ | ' ' | 信用证形式,枚举: 1 :IRREVOCABLE 2 :IRREVOCABLETRANSFERABLE |
| 33 | fopendate | 开证日期 | varchar | 50 |  | √ | ' ' | 开证日期 |
| 34 | fforwardaddress | 转通知行地址 | varchar | 255 |  | √ | ' ' | 转通知行地址 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fisregister | 登记 | bpchar | 1 |  | √ | '0' | 登记 |
| 37 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 38 | fcontractno | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 39 | fduedate | 信用证到期日 | varchar | 50 |  | √ | ' ' | 信用证到期日 |
| 40 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 41 | fcharaccno | 手续费扣费账号 | varchar | 50 |  | √ | ' ' | 手续费扣费账号 |
| 42 | fcashway | 兑付方式 | varchar | 50 |  | √ | ' ' | 兑付方式,枚举: 1 :BY PAYMENT 2 :BY ACCEPTANCE 3 :BY NEGOTIATION 4 :BY DEF PAYMENT 5 :BY MIXED PYMT |
| 43 | fbankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 44 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fapplicantaddressen | 开证申请人名称地址（英文） | varchar | 255 |  | √ | ' ' | 开证申请人名称地址（英文） |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_onlineresult |  | fid |
| 2 | idx_onlineresult_forg_fbank |  | forgid,fbankid |

---

## 开证记录查询-关联追踪表 t_lc_onlineresult_tc

- **表名称：** 开证记录查询-关联追踪表
- **表名：** t_lc_onlineresult_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_onlineresult_tc_tbill |  | ftbillid |
| 2 | pk_lc_onlineresult_tc |  | fid |
| 3 | idx_lc_onlineresult_tc_tid |  | ftid |

---

## 关联子实体-子表 t_lc_onlineresult_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_onlineresult_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_onlineresult_lk_fk |  | fid |
| 2 | pk_lc_onlineresult_lk |  | fpkid |
