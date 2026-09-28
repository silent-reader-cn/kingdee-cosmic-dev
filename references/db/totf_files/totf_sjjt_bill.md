# 计提底稿编制(废弃)-totf_sjjt_bill

## 计提底稿编制(废弃)-主表 t_tpo_declare_main_tsd

- **表名称：** 计提底稿编制(废弃)-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 5 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: sljsjj :地方水利建设基金计提底稿 dwfhf :堤围防护费计提底稿 whsyjsf :文化事业建设费计提底稿 ghjf :工会经费计提底稿 ghcbj :工会筹备金计提底稿 czljclf :城镇垃圾处理费计提底稿 cjrjybzj :残疾人就业保障金计提底稿 |
| 6 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 8 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 11 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 计提底稿编号 | varchar | 100 |  | √ | ' ' | 计提底稿编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 25 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 34 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsbbno | fsbbno | varchar | 100 |  | √ | ' ' |  |
| 48 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 51 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 56 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 57 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 58 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 59 | fdeadline | fdeadline | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tpo_declare_main_tsd |  | fid |
| 2 | idx_declare_main_tsd_fbillno |  | fbillno |
| 3 | idx_decl_main_tsd_orgid_qzme |  | forgid,fskssqq,fskssqz,ftaxsystem,faccountsettype |

---

## 计提明细-子表 t_totf_sjjt_entry

- **表名称：** 计提明细-子表
- **表名：** t_totf_sjjt_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 3 | fflhdwse | （费）率或单位税额 | numeric | 23 | 10 | √ | 0 | （费）率或单位税额 |
| 4 | fsnsjapcjrjyrsnew | 上年实际安排残疾人就业人数 | numeric | 23 | 10 | √ | 0 | 上年实际安排残疾人就业人数 |
| 5 | fysx | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 8 | fsskcs | 速算扣除数 | numeric | 23 | 10 | √ | 0 | 速算扣除数 |
| 9 | fsnzzzgnpjgz | 上年在职职工年平均工资（或当地社会平均工资的2倍） | numeric | 23 | 10 | √ | 0 | 上年在职职工年平均工资（或当地社会平均工资的2倍） |
| 10 | ffeerate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 11 | fzapcjrjybl | 应安排残疾人就业比例 | numeric | 23 | 10 | √ | 0 | 应安排残疾人就业比例 |
| 12 | fjcx | 减除项 | numeric | 23 | 10 | √ | 0 | 减除项 |
| 13 | fyssdl | 应税所得率 | numeric | 23 | 10 | √ | 0 | 应税所得率 |
| 14 | fsnzzzgrs | 上年在职职工人数（废弃） | int8 | 64 |  | √ | 0 | 上年在职职工人数（废弃） |
| 15 | fkcs | 扣除数 | numeric | 23 | 10 | √ | 0 | 扣除数 |
| 16 | fsnsjapcjrjyrs | 上年实际安排残疾人就业人数(废弃) | int8 | 64 |  | √ | 0 | 上年实际安排残疾人就业人数(废弃) |
| 17 | fzsbz | 征收标准 | numeric | 23 | 10 | √ | 0 | 征收标准 |
| 18 | fyjfe | 已缴费额 | numeric | 23 | 10 | √ | 0 | 已缴费额 |
| 19 | fsnzzzgzze | 上年在职职工工资总额 | numeric | 23 | 10 | √ | 0 | 上年在职职工工资总额 |
| 20 | fjmfe | 减免费额 | numeric | 23 | 10 | √ | 0 | 减免费额 |
| 21 | fsnzzzgrsnew | 上年在职职工人数 | numeric | 23 | 10 | √ | 0 | 上年在职职工人数 |
| 22 | fynfe | 应纳费额 | numeric | 23 | 10 | √ | 0 | 应纳费额 |
| 23 | fyzsr | 应征收入 | numeric | 23 | 10 | √ | 0 | 应征收入 |
| 24 | fyjfjs | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 25 | fjtynfe | 计提应纳费额 | numeric | 23 | 10 | √ | 0 | 计提应纳费额 |
| 26 | fjfxse | 计费销售额 | numeric | 23 | 10 | √ | 0 | 计费销售额 |
| 27 | fjfyj | 计费依据 | numeric | 23 | 10 | √ | 0 | 计费依据 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fzsbl | 征收比例 | numeric | 23 | 10 | √ | 0 | 征收比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_sjjt_entry |  | fentryid |
| 2 | idx_totf_sjjt_entry_fk |  | fid |
