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
| 4 | ftasktype | 执行内容 | int8 | 64 |  | √ | 0 | 任务类型 tsate_tasktype |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 9 | fsbqj | 申报期间 | timestamp | 0 |  |  | null | 申报期间 |
| 10 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 11 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 12 | fchannel | 申报通道 | varchar | 50 |  | √ | ' ' | 申报通道,枚举: 1 :金蝶账无忧 3 :神州云合 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 17 | fexecutestatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :成功 3 :失败 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 20 | fpiclog | 图片日志 | varchar | 255 |  | √ | ' ' | 图片日志 |
| 21 | ftype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税及附加税费 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模增值税及附加税费 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） zzsyjskb :增值税预缴税款表 xfs :烟类消费税 xfsjypf :卷烟批发消费税 xfsjl :酒类消费税 xfscpy :成品油消费税 xfsxqc :小汽车消费税 xfsdc :电池消费税 xfstl :涂料消费税 xfsqt :其他消费税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 tcvvt :车船税 tcept :环保税 tcrt :资源税 yys :烟叶税 fcscztdsys :房产和城镇土地使用税 qhjtbs :千户集团报送 zdsybsqyxxb :重点税源企业基本信息表 ccxws :财产行为税 FR0001 :财务报表（一般企业_未执行） FR0002 :财务报表（一般企业_已执行） FR0003 :财务报表（小企业会计准则） FR0004 :财务报表（企业会计制度） FR0011 :财务报表（金融企业会计准则） qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 zzsybnsr_yz_fzjg :增值税一般企业汇总申报预征方式分支机构 zzsybnsr_yz_zjg :增值税一般企业汇总申报预征方式总机构 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 zdsybs_yd :重点税源报送(月度) |
| 22 | fdeallog | 执行日志 | varchar | 255 |  | √ | ' ' | 执行日志 |
| 23 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 24 | fexecutetype | 执行内容 | varchar | 50 |  | √ | ' ' | 执行内容,枚举: ZLSB :直连申报 ZLJK :直连缴款 SBJT :申报记录 KKJT :扣款记录 WSPZ :申报凭证 TBZT :同步状态 YYJK :预约缴款 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | flogdetail | 日志详情 | varchar | 1000 |  | √ | ' ' | 日志详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_record |  | fid |
| 2 | idx_t_tsate_declare_record_1 |  | fsbbid |
| 3 | idx_tsate_declare_record |  | forgid,ftype,fskssqq,fskssqz |
