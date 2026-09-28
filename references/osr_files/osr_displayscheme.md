# 界面显示方案-osr_displayscheme

## 界面显示方案-主表 t_osr_dispscheme

- **表名称：** 界面显示方案-主表
- **表名：** t_osr_dispscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillobj | 单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 6 | fworkshoporg | 适用车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisreportatc | 汇报活动耗时 | bpchar | 1 |  | √ | '0' | 汇报活动耗时 |
| 9 | fisenableprw | 启用计件工资 | bpchar | 1 |  | √ | '1' | 启用计件工资 |
| 10 | fdefaultscheme | 默认方案 | bpchar | 1 |  | √ | '0' | 默认方案 |
| 11 | fisautoauditing | 报工后自动审核 | bpchar | 1 |  | √ | '1' | 报工后自动审核 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 界面显示方案业务类型 osr_dispschemebiztype |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fworkinginstruction | 工序计划附件 | bpchar | 1 |  | √ | '1' | 工序计划附件 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fistemplate | 系统预置模板 | bpchar | 1 |  | √ | '0' | 系统预置模板 |
| 20 | fisreportatt | 汇报附件 | bpchar | 1 |  | √ | '0' | 汇报附件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispscheme |  | fid |
| 2 | idx_osr_dispscheme |  | fcreatetime,fbiztype,fworkshoporg |

---

## 详情字段配置单据体-子表 t_osr_dispscheme_entryd

- **表名称：** 详情字段配置单据体-子表
- **表名：** t_osr_dispscheme_entryd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetialvisibility | 移动端可见性 | bpchar | 1 |  | √ | '1' | 移动端可见性 |
| 3 | fdetialfieldalias | 字段别名 | varchar | 50 |  | √ | ' ' | 字段别名 |
| 4 | fdetailformula | 公式 | varchar | 1000 |  | √ | ' ' | 公式 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetialfieldremark | 字段备注 | varchar | 200 |  | √ | ' ' | 字段备注 |
| 7 | fdetaildisplaylocation | 显示位置 | varchar | 50 |  | √ | ' ' | 显示位置,枚举: titilepanel :标题区 contentpanel :内容区 collapsearea :折叠区 |
| 8 | fdetialmdisplayname | 移动端显示名称 | varchar | 200 |  | √ | ' ' | 移动端显示名称 |
| 9 | fdetialisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fdetailiscombined | 是否组合字段 | bpchar | 1 |  | √ | '0' | 是否组合字段 |
| 11 | fdetialfieldname | 字段名称 | varchar | 200 |  | √ | ' ' | 字段名称 |
| 12 | fdetaildesignmeta | 设计期元数据 | varchar | 2000 |  | √ | ' ' | 设计期元数据 |
| 13 | fdetialmetafield | 元数据字段 | varchar | 1000 |  | √ | ' ' | 元数据字段 |
| 14 | fdetailunitfield | 单位字段 | varchar | 200 |  | √ | ' ' | 单位字段 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_osr_dispscheme_entryd |  | fentryid |
| 2 | idx_osr_dispschemed |  | fdetialmdisplayname,fdetialfieldalias |

---

## 界面显示方案-多语言表 t_osr_dispscheme_l

- **表名称：** 界面显示方案-多语言表
- **表名：** t_osr_dispscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_osr_dispscheme_l |  | fpkid |
| 2 | idx_osr_dispscheme_l |  | fid,flocaleid |

---

## 列表字段配置单据体-子表 t_osr_dispscheme_entry

- **表名称：** 列表字段配置单据体-子表
- **表名：** t_osr_dispscheme_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdesignmeta | 设计期元数据 | varchar | 2000 |  | √ | ' ' | 设计期元数据 |
| 3 | ffieldalias | 字段别名 | varchar | 50 |  | √ | ' ' | 字段别名 |
| 4 | fdisplaylocation | 显示位置 | varchar | 50 |  | √ | ' ' | 显示位置,枚举: titilepanel :标题区 contentpanel :内容区 |
| 5 | ffieldname | 字段名称 | varchar | 200 |  | √ | ' ' | 字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | funitfield | 单位字段 | varchar | 200 |  | √ | ' ' | 单位字段 |
| 8 | ffieldremark | 字段备注 | varchar | 200 |  | √ | ' ' | 字段备注 |
| 9 | fmetafield | 元数据字段 | varchar | 1000 |  | √ | ' ' | 元数据字段 |
| 10 | fvisibility | 移动端可见性 | bpchar | 1 |  | √ | '1' | 移动端可见性 |
| 11 | fiscombined | 是否组合字段 | bpchar | 1 |  | √ | '0' | 是否组合字段 |
| 12 | fmdisplayname | 移动端显示名称 | varchar | 200 |  | √ | ' ' | 移动端显示名称 |
| 13 | fformula | 公式 | varchar | 1000 |  | √ | ' ' | 公式 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_osr_dispscheme_entry |  | fentryid |
| 2 | idx_osr_dispschemee |  | fmdisplayname,ffieldalias |
