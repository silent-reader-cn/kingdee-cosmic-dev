# 底稿单据-tctb_draft_main

## 底稿单据-主表 t_tctb_draft_main

- **表名称：** 底稿单据-主表
- **表名：** t_tctb_draft_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型,枚举: |
| 10 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisdeclare | 是否生成申报表 | bpchar | 1 |  | √ | '0' | 是否生成申报表 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 14 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型 |
| 17 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 18 | fjtnumber | 计提单号 | varchar | 50 |  | √ | ' ' | 计提单号 |
| 19 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 20 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 auto :自动新增 |
| 21 | fdrafttype | 底稿类别 | varchar | 50 |  | √ | ' ' | 底稿类别,枚举: qysdsjb :企业所得税预缴底稿 qysdsnb :企业所得税年报底稿 zzs :增值税底稿 |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
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

---

## 附件字段-附件表 t_tctb_draft_main_att

- **表名称：** 附件字段-附件表
- **表名：** t_tctb_draft_main_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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
