# 图号分组-plm_plmdc_drawnogroup

## 图号规则-子表 t_plmdc_group_drawnorule

- **表名称：** 图号规则-子表
- **表名：** t_plmdc_group_drawnorule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fdrawrule | 规则名称 | int8 | 64 |  | √ | 0 | [图号规则列表 plm_plmdc_drawnorule](../plmdc_files/plm_plmdc_drawnorule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_group_drawnorule |  | fentryid |
| 2 | idx_plmdc_group_drawnorule_fk |  | fid |

---

## 图号分组-多语言表 t_plmdc_drawnogroup_l

- **表名称：** 图号分组-多语言表
- **表名：** t_plmdc_drawnogroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_drawnogroup_l |  | fpkid |
| 2 | idx_plmdc_drawnogroup_l_ |  | fid,flocaleid |

---

## 单据体-子表 t_plmdc_grouptemplate

- **表名称：** 单据体-子表
- **表名：** t_plmdc_grouptemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatestatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: waitting :等待 success :成功 error :失败 |
| 3 | ftemplateerrmsg_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 4 | ffiletype | 文件类型 | int8 | 64 |  | √ | 0 | [文件类型 plm_plmdc_file_type](../plmdc_files/plm_plmdc_file_type.md) |
| 5 | ftemplateerrmsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftemplatephysicalfile | 模板物理文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 9 | ftemplatecreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | ftemplatecreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_grouptemplate_fk |  | fid |
| 2 | pk_t_plmdc_grouptemplate |  | fentryid |

---

## 图号分组-主表 t_plmdc_drawnogroup

- **表名称：** 图号分组-主表
- **表名：** t_plmdc_drawnogroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fparentid | 父项分组 | int8 | 64 |  | √ | 0 | [图号分组 plm_plmdc_drawnogroup](../plmdc_files/plm_plmdc_drawnogroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fisdefaultrule | 是否继承 | bpchar | 1 |  | √ | '1' | 是否继承 |
| 9 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fhfiletype | 文件类型 | int8 | 64 |  | √ | 0 | [文件类型 plm_plmdc_file_type](../plmdc_files/plm_plmdc_file_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_drawnogroup |  | fid |
| 2 | idx_plmdc_drawnogroup_number |  | fnumber |
