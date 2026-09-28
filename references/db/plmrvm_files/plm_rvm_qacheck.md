# 评审目标填写-plm_rvm_qacheck

## 单据体-子表 t_plm_rvm_qaentry

- **表名称：** 单据体-子表
- **表名：** t_plm_rvm_qaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisfromdoc | 是否评审单带入 | bpchar | 1 |  | √ | '0' | 是否评审单带入 |
| 3 | ftarget_value | 目标值 | varchar | 50 |  | √ | ' ' | 目标值 |
| 4 | fdescribe | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 5 | factual_value | 实际值 | varchar | 50 |  | √ | ' ' | 实际值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fquality_obj | 质量目标 | int8 | 64 |  | √ | 0 | [质量目标 plm_qm_objectives](../plmrvm_files/plm_qm_objectives.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_qaentry |  | fentryid |
| 2 | idx_plm_rvm_qaentry_fk |  | fid |

---

## 评审目标填写-主表 t_plm_rvm_qacheck

- **表名称：** 评审目标填写-主表
- **表名：** t_plm_rvm_qacheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fque_desc | 遗留问题改进说明 | varchar | 1000 |  | √ | ' ' | 遗留问题改进说明 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | QA | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | freview_doc | 所属评审单 | int8 | 64 |  | √ | 0 | [评审单 plm_rvm_doc](../plmrvm_files/plm_rvm_doc.md) |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_qacheck |  | fid |
| 2 | idx_plm_rvm_qacheck_m0 |  | fmasterid |

---

## 评审目标填写-多语言表 t_plm_rvm_qacheck_l

- **表名称：** 评审目标填写-多语言表
- **表名：** t_plm_rvm_qacheck_l

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
| 1 | pk_plm_rvm_qacheck_l |  | fpkid |
| 2 | idx_plm_rvm_qacheck_l_0 |  | fid,flocaleid |
