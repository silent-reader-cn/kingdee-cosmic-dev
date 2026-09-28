# 附件字段-idi_attachmentfield

## 附件字段-多语言表 t_idi_attachmentfield_l

- **表名称：** 附件字段-多语言表
- **表名：** t_idi_attachmentfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 1000 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_attachmentfield_l |  | fpkid |
| 2 | idx_idi_attachmentfield_l_fid |  | fid |

---

## 附件字段-主表 t_idi_attachmentfield

- **表名称：** 附件字段-主表
- **表名：** t_idi_attachmentfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [附件模板分类 idi_fieldgroup](../idi_files/idi_fieldgroup.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | faitemplateid | 视觉服务模板 | int8 | 64 |  | √ | 0 | [模板基础资料 cvp_template_base](../cvp_files/cvp_template_base.md) |
| 7 | fsource | 字段来源 | bpchar | 1 |  | √ | ' ' | 字段来源,枚举: 0 :视觉识别服务 1 :令才科技模板 |
| 8 | ftablenumber | 令才表格字段编号 | varchar | 80 |  | √ | ' ' | 令才表格字段编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 16 | flctemplate | 令才模板名称 | varchar | 100 |  | √ | ' ' | 令才模板名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_attachmentfield |  | fid |
| 2 | idx_idi_attachmentfield_fgroup |  | fgroupid |
