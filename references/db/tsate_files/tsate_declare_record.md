# 报税任务监控-tsate_declare_record

## 报税任务监控-主表 t_tsate_declare_record

- **表名称：** 报税任务监控-主表
- **表名：** t_tsate_declare_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetaillog_tag | 详细日志_详情 | text | 0 |  |  | null | 详细日志_详情 |
| 3 | fdetaillog | 详细日志 | varchar | 255 |  | √ | ' ' | 详细日志 |
| 4 | ftasktype | 执行内容 | int8 | 64 |  | √ | 0 | [任务类型 tsate_tasktype](../tsate_files/tsate_tasktype.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdimentionindex | 业务维度索引 | varchar | 100 |  | √ | ' ' | 业务维度索引 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 10 | fsbqj | 申报期间 | timestamp | 0 |  |  | null | 申报期间 |
| 11 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fchannel | 申报通道 | varchar | 50 |  | √ | ' ' | 申报通道,枚举: 1 :金蝶账无忧 3 :神州云合 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | [申报通道 tsate_channel](../tsate_files/tsate_channel.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 18 | fexecutestatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :成功 3 :失败 0 :初始化 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | ftaskcontext | 任务上下文 | varchar | 255 |  | √ | ' ' | 任务上下文 |
| 21 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 22 | ftaskcontext_tag | 任务上下文_详情 | text | 0 |  |  | null | 任务上下文_详情 |
| 23 | fpiclog | 图片日志 | varchar | 255 |  | √ | ' ' | 图片日志 |
| 24 | ftype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税及附加税费 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模增值税及附加税费 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） zzsyjskb :增值税预缴税款表 xfs :烟类消费税 xfsjypf :卷烟批发消费税 xfsjl :酒类消费税 xfscpy :成品油消费税 xfsxqc :小汽车消费税 xfsdc :电池消费税 xfstl :涂料消费税 xfsqt :其他消费税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 tcvvt :车船税 tcept :环保税 tcrt :资源税 yys :烟叶税 fcscztdsys :房产和城镇土地使用税 qhjtbs :千户集团报送 zdsybsqyxxb :重点税源企业基本信息表 ccxws :财产行为税 FR0001 :财务报表（一般企业_未执行） FR0002 :财务报表（一般企业_已执行） FR0003 :财务报表（小企业会计准则） FR0004 :财务报表（企业会计制度） FR0011 :财务报表（金融企业会计准则） qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 zzsybnsr_yz_fzjg :增值税一般企业汇总申报预征方式分支机构 zzsybnsr_yz_zjg :增值税一般企业汇总申报预征方式总机构 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 zdsybs_yd :重点税源报送(月度) zdsybs_jd :重点税源表（季度） whsyjsf :文化事业建设费 xfsjfj :消费税及附加 totf_cjrjybzj :残疾人就业保障金缴费申报表 globaltax_sg_sbb :海外税-新加坡申报表 iit_zhsd_sbb :个人所得税综合所得申报表 globaltax_sg_qysd_sbb :海外税-新加坡企业所得税 |
| 25 | fdeallog | 执行日志 | varchar | 255 |  | √ | ' ' | 执行日志 |
| 26 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 27 | fexecutetype | 执行内容 | varchar | 50 |  | √ | ' ' | 执行内容,枚举: ZLSB :直连申报 ZLJK :直连缴款 SBJT :申报记录 KKJT :扣款记录 WSPZ :申报凭证 TBZT :同步状态 YYJK :预约缴款 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | flogdetail | 日志详情 | varchar | 1000 |  | √ | ' ' | 日志详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_record |  | fid |
| 2 | idx_t_taste_declare_record_3 |  | fdimentionindex |
| 3 | idx_t_tsate_declare_record_1 |  | fsbbid |
| 4 | idx_tsate_declare_record |  | forgid,ftype,fskssqq,fskssqz |
| 5 | idx_t_tsate_declare_record_2 |  | fcreatetime,fexecutetype |
