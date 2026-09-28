# 底稿列表-tam_draft_bill

## 底稿列表-主表 t_tctb_draft_main

- **表名称：** 底稿列表-主表
- **表名：** t_tctb_draft_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | ftemplatetype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: draft_qysdsjb :企业所得税预缴 draft_qysdsnb :企业所得税年报 draft_zzsybnsr :一般纳税人增值税 draft_zzsxgmnsr :小规模纳税人增值税 draft_zzsybnsr_ybhz :汇总一般企业增值税 draft_zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 draft_zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 |
| 10 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisdeclare | 是否生成申报表 | bpchar | 1 |  | √ | '0' | 是否生成申报表 |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftype | ftype | varchar | 36 |  | √ | ' ' |  |
| 17 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 18 | fjtnumber | fjtnumber | varchar | 50 |  | √ | ' ' |  |
| 19 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 20 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 auto :自动新增 |
| 21 | fdrafttype | 底稿类别 | varchar | 50 |  | √ | ' ' | 底稿类别,枚举: qysdsjb :企业所得税预缴底稿 qysdsnb :企业所得税年报底稿 zzs :增值税底稿 |
| 22 | fbillno | 底稿编号 | varchar | 30 |  | √ | ' ' | 底稿编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fsbbno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_draft_main |  | forgid,ftemplatetype,fstartdate,fenddate,fbillno |
| 2 | pk_tctb_draft_main |  | fid |
