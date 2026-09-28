# 底稿2.0代理-bdtaxr_draft_proxy

## 底稿2.0代理-主表 t_tctb_draft_main

- **表名称：** 底稿2.0代理-主表
- **表名：** t_tctb_draft_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faccrualplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 5 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 6 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型,枚举: |
| 7 | fsteplevel | 汇总层级 | varchar | 50 |  | √ | ' ' | 汇总层级,枚举: root :根节点 middle :中间节点 leaf :叶子节点 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 10 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fjtnumber | 计提单号 | varchar | 50 |  | √ | ' ' | 计提单号 |
| 13 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 14 | fflexbizdims | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fdrafttype | 底稿类别 | varchar | 50 |  | √ | ' ' | 底稿类别,枚举: qysdsjb :企业所得税预缴底稿 qysdsnb :企业所得税年报底稿 zzs :增值税底稿 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fsbbno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fstepsummary | 逐级汇总 | bpchar | 1 |  | √ | '0' | 逐级汇总 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 24 | fstepparentid | 汇总父级报表id | int8 | 64 |  | √ | 0 | 汇总父级报表id |
| 25 | fisdeclare | 是否生成申报表 | bpchar | 1 |  | √ | '0' | 是否生成申报表 |
| 26 | fdataversion | fdataversion | varchar | 50 |  | √ | ' ' |  |
| 27 | ftype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型 |
| 28 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 29 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 30 | fdeadline | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 31 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 auto :自动新增 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_draft_main |  | forgid,ftemplatetype,fstartdate,fenddate,fbillno |
| 2 | pk_tctb_draft_main |  | fid |

---

## 附件字段-附件表 t_tctb_draft_main_att

- **表名称：** 附件字段-附件表
- **表名：** t_tctb_draft_main_att

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
| 1 | pk_tctb_draft_main_att |  | fpkid |
| 2 | idx_t_tctb_draft_main_att_fid |  | fid |
