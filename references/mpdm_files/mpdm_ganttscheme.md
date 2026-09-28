# 甘特图方案-mpdm_ganttscheme

## 甘特图方案-主表 t_mpdm_ganttscheme

- **表名称：** 甘特图方案-主表
- **表名：** t_mpdm_ganttscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmaxlevel | 任务最大层级 | int4 | 32 |  | √ | 0 | 任务最大层级 |
| 5 | foperatorclass | 操作器实现类 | varchar | 80 |  | √ | ' ' | 操作器实现类 |
| 6 | fdataentityid | 数据实体 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fimporterclass | 导入器实现类 | varchar | 80 |  | √ | ' ' | 导入器实现类 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 10 | ftaskentityid | 任务实体 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fquerierclass | 查询器实现类 | varchar | 80 |  | √ | ' ' | 查询器实现类 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fexporterclass | 导出器实现类 | varchar | 80 |  | √ | ' ' | 导出器实现类 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fconvertorclass | 转换器实现类 | varchar | 80 |  | √ | ' ' | 转换器实现类 |
| 18 | fconfigentityid | 配置实体 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fmaxcount | 任务最大数量 | int4 | 32 |  | √ | 0 | 任务最大数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ganttscheme |  | fid |
| 2 | idx_mpdm_gs_number |  | fnumber |

---

## 控件定义-子表 t_mpdm_ganttschemecontrol

- **表名称：** 控件定义-子表
- **表名：** t_mpdm_ganttschemecontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fiscontrolpreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fganttcontrol | 甘特图控件 | varchar | 50 |  | √ | ' ' | 甘特图控件 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_gsc_bo |  | fbizobjectid |
| 2 | pk_mpdm_ganttschemecontrol |  | fentryid |
| 3 | idx_mpdm_gsc_id |  | fid |

---

## 关联字段-子表 t_mpdm_ganttschemerelate

- **表名称：** 关联字段-子表
- **表名：** t_mpdm_ganttschemerelate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frelatecolumn | 关联列名 | varchar | 50 |  | √ | ' ' | 关联列名 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_gsr_eid |  | fentryid |
| 2 | pk_mpdm_ganttschemerelate |  | fdetailid |

---

## 字段定义-子表 t_mpdm_ganttschemefield

- **表名称：** 字段定义-子表
- **表名：** t_mpdm_ganttschemefield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefaultalign | 默认对齐方式 | bpchar | 1 |  | √ | ' ' | 默认对齐方式,枚举: l :居左 c :居中 r :居右 d :默认 |
| 3 | flabel | 标题 | varchar | 200 |  | √ | ' ' | 标题 |
| 4 | fisfieldpreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 5 | fcolumn | 列名 | varchar | 50 |  | √ | ' ' | 列名 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | feditable | 允许编辑 | bpchar | 1 |  | √ | ' ' | 允许编辑 |
| 8 | fdefaultvisible | 默认可见 | bpchar | 1 |  | √ | ' ' | 默认可见 |
| 9 | frequired | 必要 | bpchar | 1 |  | √ | ' ' | 必要 |
| 10 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: t :文本 n :数值 d :日期 s :下拉列表 m :表单 f :F7 c :复选框 |
| 11 | fdefaultwidth | 默认宽度 | int4 | 32 |  | √ | 0 | 默认宽度 |
| 12 | fimportable | 允许引入 | bpchar | 1 |  | √ | ' ' | 允许引入 |
| 13 | fentityfield | 实体字段 | varchar | 50 |  | √ | ' ' | 实体字段 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ganttschemefield |  | fentryid |
| 2 | idx_mpdm_gsf_id |  | fid |

---

## 甘特图方案-多语言表 t_mpdm_ganttscheme_l

- **表名称：** 甘特图方案-多语言表
- **表名：** t_mpdm_ganttscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ganttscheme_l |  | fpkid |
| 2 | idx_mpdm_gs_l |  | fid,flocaleid |

---

## 字段定义-多语言表 t_mpdm_ganttschemefield_l

- **表名称：** 字段定义-多语言表
- **表名：** t_mpdm_ganttschemefield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flabel | 标题 | varchar | 200 |  | √ | ' ' | 标题 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_gsf_l |  | fentryid,flocaleid |
| 2 | pk_mpdm_ganttschemefield_l |  | fpkid |
