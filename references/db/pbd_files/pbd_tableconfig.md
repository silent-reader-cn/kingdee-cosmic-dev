# 表格数据配置方案-pbd_tableconfig

## 小计单据体-多语言表 t_pbd_sumentry_l

- **表名称：** 小计单据体-多语言表
- **表名：** t_pbd_sumentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsumfieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 2 | fsumdisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_sumentry_l_fid |  | fentryid,flocaleid |
| 2 | pk_pbd_sumentry_l |  | fpkid |

---

## 对比项单据体-多语言表 t_pbd_splitentry_l

- **表名称：** 对比项单据体-多语言表
- **表名：** t_pbd_splitentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsplitdisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsplitfieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_splitentry_l_fid |  | fentryid,flocaleid |
| 2 | pk_pbd_splitentry_l |  | fpkid |

---

## 聚合单据体-多语言表 t_pbd_mergeentry_l

- **表名称：** 聚合单据体-多语言表
- **表名：** t_pbd_mergeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmergefieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fmergedisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_mergeentry_l |  | fpkid |
| 2 | idx_pbd_mergeentry_l_fid |  | fentryid,flocaleid |

---

## 行列分组单据体-多语言表 t_pbd_groupentry_l

- **表名称：** 行列分组单据体-多语言表
- **表名：** t_pbd_groupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffiltername | 筛选分组名称 | varchar | 100 |  | √ | ' ' | 筛选分组名称 |
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
| 1 | idx_pbd_groupentry_l_fid |  | fentryid,flocaleid |
| 2 | pk_pbd_groupentry_l |  | fpkid |

---

## 小计单据体-子表 t_pbd_sumentry

- **表名称：** 小计单据体-子表
- **表名：** t_pbd_sumentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumrange | 取值范围 | bpchar | 1 |  | √ | '0' | 取值范围,枚举: 1 :全部数据 2 :选择数据 |
| 3 | fsumfieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 4 | fsumdisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 5 | fformat | 显示格式 | varchar | 100 |  | √ | ' ' | 显示格式 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fisfiltersum | 默认显示 | bpchar | 1 |  | √ | '0' | 默认显示 |
| 8 | fparamtype | 参数类型 | bpchar | 1 |  | √ | '0' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉选 |
| 9 | fsumfieldkey | 选择字段 | varchar | 100 |  | √ | ' ' | 选择字段,枚举: |
| 10 | fissumcustom | 自定义列 | bpchar | 1 |  | √ | '0' | 自定义列 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fsumprokey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 13 | fsumtype | 聚合类型 | bpchar | 1 |  | √ | '0' | 聚合类型,枚举: 1 :求和 2 :平均值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_sumentry |  | fentryid |
| 2 | idx_pbd_sumentry_fid |  | fid |

---

## 对比项单据体-子表 t_pbd_splitentry

- **表名称：** 对比项单据体-子表
- **表名：** t_pbd_splitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissplitcustom | 自定义列 | bpchar | 1 |  | √ | '0' | 自定义列 |
| 3 | fsplitdisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 4 | fisfiltersplit | 默认显示 | bpchar | 1 |  | √ | '0' | 默认显示 |
| 5 | fformat | 显示格式 | varchar | 50 |  | √ | ' ' | 显示格式 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsplitfieldkey | 选择字段 | varchar | 100 |  | √ | ' ' | 选择字段,枚举: |
| 8 | fparamtype | 参数类型 | bpchar | 1 |  | √ | '0' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉选 |
| 9 | fsplitprokey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsplitfieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_splitentry |  | fentryid |
| 2 | idx_pbd_splitentry_fid |  | fid |

---

## 行列分组单据体-子表 t_pbd_groupentry

- **表名称：** 行列分组单据体-子表
- **表名：** t_pbd_groupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltername | 筛选分组名称 | varchar | 100 |  | √ | ' ' | 筛选分组名称 |
| 3 | fgroupkey | 分组取值字段 | varchar | 100 |  | √ | ' ' | 分组取值字段,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fisfiltergroup | 是否筛选 | bpchar | 1 |  | √ | '0' | 是否筛选 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fgrouptype | 分组类型 | bpchar | 1 |  | √ | '2' | 分组类型,枚举: 1 :行分组 2 :列分组 |
| 8 | fgroupname | 分组名称取值字段 | varchar | 100 |  | √ | ' ' | 分组名称取值字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_groupentry |  | fentryid |
| 2 | idx_pbd_groupentry_fid |  | fid |

---

## 聚合单据体-子表 t_pbd_mergeentry

- **表名称：** 聚合单据体-子表
- **表名：** t_pbd_mergeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmergefieldkey | 选择字段 | varchar | 100 |  | √ | ' ' | 选择字段,枚举: |
| 3 | fmergeprokey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 4 | fformat | 显示格式 | varchar | 50 |  | √ | ' ' | 显示格式 |
| 5 | fismergecustom | 自定义列 | bpchar | 1 |  | √ | '0' | 自定义列 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmergefieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | fparamtype | 参数类型 | bpchar | 1 |  | √ | '0' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉选 |
| 9 | fisfiltermerge | 默认显示 | bpchar | 1 |  | √ | '0' | 默认显示 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmergedisplayname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_mergeentry |  | fentryid |
| 2 | idx_pbd_mergeentry_fid |  | fid |

---

## 表格数据配置方案-主表 t_pbd_tableconfig

- **表名称：** 表格数据配置方案-主表
- **表名：** t_pbd_tableconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcondition_tag | 条件对象(后台字段)_详情 | text | 0 |  |  | null | 条件对象(后台字段)_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbizobject | 对应的业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmaxsize | 最大显示数据 | int4 | 32 |  | √ | 0 | 最大显示数据 |
| 9 | fsumname | 合计名称 | varchar | 100 |  | √ | ' ' | 合计名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbizappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmergename | 聚合名称 | varchar | 100 |  | √ | ' ' | 聚合名称 |
| 16 | fsplitname | 分项名称 | varchar | 100 |  | √ | ' ' | 分项名称 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fcondition | 条件对象(后台字段) | varchar | 510 |  | √ | ' ' | 条件对象(后台字段) |
| 19 | fplugin | 插件 | varchar | 225 |  | √ | ' ' | 插件 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | forderby | 排序 | varchar | 500 |  | √ | ' ' | 排序 |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 23 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_tableconfig |  | fid |
| 2 | idx_pbd_tableconfig_fnumber |  | fnumber |

---

## 表格数据配置方案-多语言表 t_pbd_tableconfig_l

- **表名称：** 表格数据配置方案-多语言表
- **表名：** t_pbd_tableconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmergename | 聚合名称 | varchar | 100 |  | √ | ' ' | 聚合名称 |
| 4 | fsplitname | 分项名称 | varchar | 100 |  | √ | ' ' | 分项名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fsumname | 合计名称 | varchar | 100 |  | √ | ' ' | 合计名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_tableconfig_l |  | fpkid |
| 2 | idx_pbd_tableconfig_l_fid |  | fid,flocaleid |
| 3 | idx_pbd_tableconfig_l_fname |  | fname |
