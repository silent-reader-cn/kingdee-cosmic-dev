# 税企直连-申报信息记录-tsate_declare_status_info

## 税企直连-申报信息记录-主表 t_tsate_declare_request

- **表名称：** 税企直连-申报信息记录-主表
- **表名：** t_tsate_declare_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequesttype | 请求类型 | varchar | 50 |  | √ | '1' | 请求类型,枚举: 1 :申报 2 :缴款 3 :转开凭证 4 :采集税务信息（税局校验） 5 :申报作废 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdetailinfo | 状态信息 | varchar | 510 |  | √ | ' ' | 状态信息 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdetailinfo_tag | 状态信息_详情 | text | 0 |  |  | null | 状态信息_详情 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fexecutestatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :成功 3 :失败 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | frecordid | 申报监控记录ID | varchar | 50 |  | √ | ' ' | 申报监控记录ID |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 16 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 17 | frequestid | 请求ID | varchar | 400 |  | √ | ' ' | 请求ID |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fnsrtype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型,枚举: zzsybnsr :一般纳税人增值税 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模纳税人增值税 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） xfs :烟类消费税 xfsjypf :卷烟批发消费税 xfsjl :酒类消费税 xfscpy :成品油消费税 xfsxqc :小汽车消费税 xfsdc :电池消费税 xfstl :涂料消费税 xfsqt :其他消费税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 tcvvt :车船税 tcept :环保税 tcrt :资源税 yys :烟叶税 fcscztdsys :房产和城镇土地使用税 qhjtbs :千户集团 zdsybsqyxxb :重点税源 |
| 21 | fchanelid | 申报通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_request |  | fid |
| 2 | index_union_key |  | forgid,fnsrtype,fskssqq,fskssqz |
