# 同步日志-tsate_dyn_log

## 同步日志-主表 t_tsate_declare_record

- **表名称：** 同步日志-主表
- **表名：** t_tsate_declare_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetaillog_tag | 详细日志_详情 | text | 0 |  |  | null | 详细日志_详情 |
| 3 | fdetaillog | 详细日志 | varchar | 255 |  | √ | ' ' | 详细日志 |
| 4 | ftasktype | 执行内容 | int8 | 64 |  | √ | 0 | [任务类型 tsate_tasktype](../tsate_files/tsate_tasktype.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdimentionindex | fdimentionindex | varchar | 100 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 10 | fsbqj | 申报期间 | timestamp | 0 |  |  | null | 申报期间 |
| 11 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fchannel | 申报通道 | varchar | 50 |  | √ | ' ' | 申报通道,枚举: 1 :金蝶账无忧 3 :神州云合 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | [申报通道 tsate_channel](../tsate_files/tsate_channel.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 18 | fexecutestatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :成功 3 :失败 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | ftaskcontext | ftaskcontext | varchar | 255 |  | √ | ' ' |  |
| 21 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 22 | ftaskcontext_tag | ftaskcontext_tag | text | 0 |  |  | null |  |
| 23 | fpiclog | fpiclog | varchar | 255 |  | √ | ' ' |  |
| 24 | ftype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模纳税人增值税 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） xfs :烟类消费税 xfsjypf :卷烟批发消费税 xfsjl :酒类消费税 xfscpy :成品油消费税 xfsxqc :小汽车消费税 xfsdc :电池消费税 xfstl :涂料消费税 xfsqt :其他消费税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 tcvvt :车船税 tcept :环保税 tcrt :资源税 yys :烟叶税 fcscztdsys :房产和城镇土地使用税 qhjtbs :千户集团 zdsybsqyxxb :重点税源 ccxws :财产行为税 |
| 25 | fdeallog | 执行日志 | varchar | 255 |  | √ | ' ' | 执行日志 |
| 26 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 27 | fexecutetype | 执行内容 | varchar | 50 |  | √ | ' ' | 执行内容,枚举: TBSH :同步税号 TBYH :同步用户 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | flogdetail | flogdetail | varchar | 1000 |  | √ | ' ' |  |

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
