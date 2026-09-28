# 我的培训-src_myexperttrain

## 证书附件-附件表 t_src_experttrain_fj

- **表名称：** 证书附件-附件表
- **表名：** t_src_experttrain_fj

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
| 1 | t_src_experttrain_fj_fid |  | fid |
| 2 | pk_src_experttrain_fj |  | fpkid |

---

## 我的培训-主表 t_src_experttrain

- **表名称：** 我的培训-主表
- **表名：** t_src_experttrain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | faddress | 培训地址 | varchar | 255 |  | √ | ' ' | 培训地址 |
| 4 | faptitudename | 证书名称 | varchar | 255 |  | √ | ' ' | 证书名称 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisselfhelp | 是否专家自助 | bpchar | 1 |  | √ | '0' | 是否专家自助 |
| 9 | fenddate | 培训时间至 | timestamp | 0 |  |  | null | 培训时间至 |
| 10 | faptitudenumber | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | faptitudetypeid | 证书类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 13 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 培训编号 | varchar | 30 |  | √ | ' ' | 培训编号 |
| 15 | fgrade | 证书等级 | varchar | 50 |  | √ | ' ' | 证书等级 |
| 16 | fitemtypeid | 培训类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 17 | fbizorg | 培训单位 | varchar | 255 |  | √ | ' ' | 培训单位 |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdateto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 21 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 23 | fischanged | 本证书是否更新到专家库 | bpchar | 1 |  | √ | '0' | 本证书是否更新到专家库 |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fbegindate | 培训时间从 | timestamp | 0 |  |  | null | 培训时间从 |
| 28 | faptitudenote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fdescription | 培训内容 | varchar | 1020 |  | √ | ' ' | 培训内容 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 35 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 36 | fitemname | 培训主题 | varchar | 255 |  | √ | ' ' | 培训主题 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_experttrain |  | fid |
| 2 | idx_src_experttrain_fbillno |  | fbillno |
| 3 | idx_src_experttrain_fexpertid |  | fexpertid |
