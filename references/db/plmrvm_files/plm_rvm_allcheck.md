# 评审自检裁决-plm_rvm_allcheck

## 单据体-子表 t_plm_rvm_checkentry

- **表名称：** 单据体-子表
- **表名：** t_plm_rvm_checkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcheck_person | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fcomments | 评审意见 | varchar | 255 |  | √ | ' ' | 评审意见 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsituation | 满足情况 | varchar | 50 |  | √ | ' ' | 满足情况,枚举: 1 :完全满足 2 :大部分满足，风险可控 3 :部分满足，风险不可控 4 :不满足 5 :不涉及 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_checkentry_fk |  | fid |
| 2 | pk_plm_rvm_checkentry |  | fentryid |

---

## 评审自检裁决-主表 t_plm_rvm_selfchecksum

- **表名称：** 评审自检裁决-主表
- **表名：** t_plm_rvm_selfchecksum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 评审点 | int8 | 64 |  | √ | 0 | [评审点 plm_qm_review_point](../plmrvm_files/plm_qm_review_point.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | freview_doc | 所属评审单 | int8 | 64 |  | √ | 0 | [评审单 plm_rvm_doc](../plmrvm_files/plm_rvm_doc.md) |
| 7 | frvm_review | 评审要素 | int8 | 64 |  | √ | 0 | [评审要素 plm_qm_review_elements](../plmrvm_files/plm_qm_review_elements.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcon_result | 仲裁结果 | varchar | 50 |  | √ | ' ' | 仲裁结果,枚举: A :完全满足 B :大部分满足，风险可控 C :部分满足，风险不可控 D :不满足 E :不涉及 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fcon_desc | 仲裁意见 | varchar | 1000 |  | √ | ' ' | 仲裁意见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_selfchecksum |  | fid |
| 2 | idx_plm_rvm_selfchecksum_m0 |  | fmasterid |

---

## 评审自检裁决-多语言表 t_plm_rvm_selfchecksum_l

- **表名称：** 评审自检裁决-多语言表
- **表名：** t_plm_rvm_selfchecksum_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_selfchecksum_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rvm_selfchecksum_l |  | fpkid |
