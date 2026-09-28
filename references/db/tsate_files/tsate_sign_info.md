# 税企直连-标识信息-tsate_sign_info

## 税企直连-标识信息-主表 t_tsate_sign_info

- **表名称：** 税企直连-标识信息-主表
- **表名：** t_tsate_sign_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsjfkstatus | 税局反馈 | varchar | 50 |  | √ | ' ' | 税局反馈,枚举: 0 :待处理 1 :已处理 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fsjfkxx_tag | 反馈信息_详情 | text | 0 |  |  | null | 反馈信息_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frecordid | 申报监控记录ID | varchar | 50 |  | √ | ' ' | 申报监控记录ID |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | fqcstatus | 获取期初状态 | varchar | 50 |  | √ | ' ' | 获取期初状态,枚举: 0 :未获取 1 :获取成功 2 :获取失败 |
| 15 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 16 | fsjfkxx | 反馈信息 | varchar | 255 |  | √ | ' ' | 反馈信息 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fnsrtype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型,枚举: zzsybnsr :一般纳税人增值税 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模纳税人增值税 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） xfs :烟类消费税 xfsjypf :卷烟批发消费税 xfsjl :酒类消费税 xfscpy :成品油消费税 xfsxqc :小汽车消费税 xfsdc :电池消费税 xfstl :涂料消费税 xfsqt :其他消费税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 tcvvt :车船税 tcept :环保税 tcrt :资源税 yys :烟叶税 fcscztdsys :房产和城镇土地使用税 qhjtbs :千户集团 zdsybsqyxxb :重点税源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_sign_info |  | forgid,fskssqq,fskssqz,fnsrtype |
| 2 | pk_tsate_sign_info |  | fid |
