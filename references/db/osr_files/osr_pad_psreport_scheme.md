# （废弃）平板工序报工显示方案-osr_pad_psreport_scheme

## 区域显示配置分录-子表 t_osr_dispscheme_entrya

- **表名称：** 区域显示配置分录-子表
- **表名：** t_osr_dispscheme_entrya

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fareafieldname | 区域名称 | varchar | 500 |  | √ | ' ' | 区域名称 |
| 3 | fareavisibility | 可见性 | bpchar | 1 |  | √ | '1' | 可见性 |
| 4 | fareadisplaylocation | 区域 | varchar | 50 |  | √ | ' ' | 区域,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fareafieldremark | 区域备注 | varchar | 1000 |  | √ | ' ' | 区域备注 |
| 7 | fareafieldkey | 区域标识 | varchar | 100 |  | √ | ' ' | 区域标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fareaisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | osr_dispscheme_entrya_idx_fid |  | fid |
| 2 | pk_t_osr_dispscheme_entrya |  | fentryid |
| 3 | osr_dispscheme_entrya_idx |  | fseq,fareafieldname,fareafieldkey |

---

## 编辑页面配置分录-多语言表 t_osr_dispscheme_entrye_l

- **表名称：** 编辑页面配置分录-多语言表
- **表名：** t_osr_dispscheme_entrye_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | feditdisplaylname | 所属区域 | varchar | 1500 |  | √ | ' ' | 所属区域 |
| 2 | feditfieldname | 字段名 | varchar | 1500 |  | √ | ' ' | 字段名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | feditfieldremark | 字段备注 | varchar | 3000 |  | √ | ' ' | 字段备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispscheme_entrye_l |  | fpkid |
| 2 | osr_dispscheme_entrye_l_idx |  | fentryid,flocaleid |

---

## （废弃）平板工序报工显示方案-主表 t_osr_dispscheme

- **表名称：** （废弃）平板工序报工显示方案-主表
- **表名：** t_osr_dispscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillobj | 单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 6 | fworkshoporg | 适用车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisreportatc | 汇报活动耗时 | bpchar | 1 |  | √ | '0' | 汇报活动耗时 |
| 9 | fisenableprw | 启用计件工资 | bpchar | 1 |  | √ | '1' | 启用计件工资 |
| 10 | fdefaultscheme | 发布 | bpchar | 1 |  | √ | '0' | 发布 |
| 11 | fisautoauditing | 报工后自动审核 | bpchar | 1 |  | √ | '1' | 报工后自动审核 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flocale | 语言 | varchar | 10 |  | √ | ' ' | 语言,枚举: zh-CN :中文 en-US :英文 zh-TW :繁体 vi-VN :越南语 |
| 14 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [界面显示方案业务类型 osr_dispschemebiztype](../osr_files/osr_dispschemebiztype.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fworkinginstruction | 工序计划附件 | bpchar | 1 |  | √ | '1' | 工序计划附件 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fistemplate | 系统预置模板 | bpchar | 1 |  | √ | '0' | 系统预置模板 |
| 21 | fisreportatt | 汇报附件 | bpchar | 1 |  | √ | '0' | 汇报附件 |

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
| 3 | fdetialfieldalias | 字段别名 | varchar | 100 |  | √ | ' ' | 字段别名 |
| 4 | fdetailformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetialfieldremark | 字段备注 | varchar | 1000 |  | √ | ' ' | 字段备注 |
| 7 | fdetaildisplaylocation | 显示位置 | varchar | 50 |  | √ | ' ' | 显示位置,枚举: titilepanel :标题区 contentpanel :内容区 collapsearea :折叠区 |
| 8 | fdetialmdisplayname | 移动端显示名称 | varchar | 500 |  | √ | ' ' | 移动端显示名称 |
| 9 | fdetialisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fdetailgrouptype | 分组方式 | varchar | 50 |  | √ | ' ' | 分组方式,枚举: concat :拼接 average :平均 sum :汇总 max :最大值 min :最小值 count :计数 |
| 11 | fdetailiscombined | 是否组合字段 | bpchar | 1 |  | √ | '0' | 是否组合字段 |
| 12 | fdetialfieldname | 字段名称 | varchar | 500 |  | √ | ' ' | 字段名称 |
| 13 | fdetailshowtitle | 是否显示标题 | bpchar | 1 |  | √ | '1' | 是否显示标题 |
| 14 | fdetaildesignmeta | 设计期元数据 | varchar | 2000 |  | √ | ' ' | 设计期元数据 |
| 15 | fdetailisgroupfield | 是否分组字段 | bpchar | 1 |  | √ | '0' | 是否分组字段 |
| 16 | fdetialmetafield | 元数据字段 | varchar | 2000 |  | √ | ' ' | 元数据字段 |
| 17 | fdetailunitfield | 引用字段 | varchar | 500 |  | √ | ' ' | 引用字段 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 区域显示配置分录-多语言表 t_osr_dispscheme_entrya_l

- **表名称：** 区域显示配置分录-多语言表
- **表名：** t_osr_dispscheme_entrya_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fareafieldname | 区域名称 | varchar | 1500 |  | √ | ' ' | 区域名称 |
| 2 | fareafieldremark | 区域备注 | varchar | 2000 |  | √ | ' ' | 区域备注 |
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
| 1 | osr_dispscheme_entrya_l_idx |  | fentryid,flocaleid |
| 2 | pk_t_osr_dispscheme_entrya_l |  | fpkid |

---

## 编辑页面配置分录-子表 t_osr_dispscheme_entrye

- **表名称：** 编辑页面配置分录-子表
- **表名：** t_osr_dispscheme_entrye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feditdefvisibility | 默认可见性 | bpchar | 1 |  | √ | '1' | 默认可见性 |
| 3 | feditisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 4 | feditfieldkey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 5 | feditdisplaylname | 所属区域 | varchar | 500 |  | √ | '' | 所属区域 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | feditdisplaylocation | 所属区域 | varchar | 50 |  | √ | '' | 所属区域,枚举: |
| 8 | feditfieldname | 字段名 | varchar | 500 |  | √ | ' ' | 字段名 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | feditvisibility | 移动端可见性 | bpchar | 1 |  | √ | '1' | 移动端可见性 |
| 11 | feditformid | 所属表单 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 12 | feditfieldremark | 字段备注 | varchar | 1000 |  | √ | ' ' | 字段备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispscheme_entrye |  | fentryid |
| 2 | osr_dispscheme_entrye_idx |  | fseq,feditfieldname,feditfieldkey,feditformid |
| 3 | osr_dispscheme_entrye_idx_fid |  | fid |

---

## 详情字段配置单据体-多语言表 t_osr_dispscheme_entryd_l

- **表名称：** 详情字段配置单据体-多语言表
- **表名：** t_osr_dispscheme_entryd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetialfieldname | 字段名称 | varchar | 1500 |  | √ | ' ' | 字段名称 |
| 2 | fdetailformula | 公式 | varchar | 3000 |  | √ | ' ' | 公式 |
| 3 | fdetialfieldremark | 字段备注 | varchar | 3000 |  | √ | ' ' | 字段备注 |
| 4 | fdetaildesignmeta | 设计期元数据 | varchar | 3000 |  | √ | ' ' | 设计期元数据 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdetialmetafield | 元数据字段 | varchar | 3000 |  | √ | ' ' | 元数据字段 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fdetialmdisplayname | 移动端显示名称 | varchar | 1500 |  | √ | ' ' | 移动端显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_osr_dispscheme_entryd_l_idx |  | fentryid,flocaleid |
| 2 | pk_t_osr_dispscheme_entryd_l |  | fpkid |

---

## 配置项单据体-子表 t_osr_dispscheme_entryc

- **表名称：** 配置项单据体-子表
- **表名：** t_osr_dispscheme_entryc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftipstitle | 帮助提示标题 | varchar | 152 |  | √ | ' ' | 帮助提示标题 |
| 3 | fconfigkey | 配置项标识 | varchar | 80 |  | √ | ' ' | 配置项标识 |
| 4 | fconfigvalue | 配置值 | varchar | 200 |  | √ | ' ' | 配置值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fconfigname | 配置项名称 | varchar | 152 |  | √ | ' ' | 配置项名称 |
| 7 | fconfigdfvalue | 默认值 | varchar | 600 |  | √ | ' ' | 默认值 |
| 8 | ftipscontent | 帮助提示内容 | varchar | 300 |  | √ | ' ' | 帮助提示内容 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fconfigtype | 配置项类型 | varchar | 80 |  | √ | ' ' | 配置项类型,枚举: number :数值 text :文本 boolean :布尔 enum :枚举 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | osr_dispscheme_entryc_idx |  | fconfigname,fconfigkey |
| 2 | pk_t_osr_dispscheme_entryc |  | fentryid |

---

## （废弃）平板工序报工显示方案-多语言表 t_osr_dispscheme_l

- **表名称：** （废弃）平板工序报工显示方案-多语言表
- **表名：** t_osr_dispscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 240 |  | √ | ' ' | 方案名称 |
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

## 列表字段配置单据体-多语言表 t_osr_dispscheme_entry_l

- **表名称：** 列表字段配置单据体-多语言表
- **表名：** t_osr_dispscheme_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdesignmeta | 设计期元数据 | varchar | 3000 |  | √ | ' ' | 设计期元数据 |
| 2 | fmdisplayname | 移动端显示名称 | varchar | 1500 |  | √ | ' ' | 移动端显示名称 |
| 3 | ffieldname | 字段名称 | varchar | 1500 |  | √ | ' ' | 字段名称 |
| 4 | fformula | 公式 | varchar | 3000 |  | √ | ' ' | 公式 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | ffieldremark | 字段备注 | varchar | 3000 |  | √ | ' ' | 字段备注 |
| 7 | fmetafield | 元数据字段 | varchar | 3000 |  | √ | ' ' | 元数据字段 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_osr_dispscheme_entry_l_idx |  | fentryid,flocaleid |
| 2 | pk_t_osr_dispscheme_entry_l |  | fpkid |

---

## 适用车间-多选基础资料表 t_osr_dispscheme_org

- **表名称：** 适用车间-多选基础资料表
- **表名：** t_osr_dispscheme_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | osr_dispscheme_org_idx |  | fid,fbasedataid |
| 2 | pk_t_osr_dispscheme_org |  | fpkid |

---

## 列表字段配置单据体-子表 t_osr_dispscheme_entry

- **表名称：** 列表字段配置单据体-子表
- **表名：** t_osr_dispscheme_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdesignmeta | 设计期元数据 | varchar | 2000 |  | √ | ' ' | 设计期元数据 |
| 3 | ffieldalias | 字段别名 | varchar | 100 |  | √ | ' ' | 字段别名 |
| 4 | fdisplaylocation | 显示位置 | varchar | 50 |  | √ | ' ' | 显示位置,枚举: titilepanel :标题区 contentpanel :内容区 collapsearea :折叠区 |
| 5 | fshowtitle | 是否显示标题 | bpchar | 1 |  | √ | '1' | 是否显示标题 |
| 6 | ffieldname | 字段名称 | varchar | 500 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | funitfield | 引用字段 | varchar | 500 |  | √ | ' ' | 引用字段 |
| 9 | ffieldremark | 字段备注 | varchar | 1000 |  | √ | ' ' | 字段备注 |
| 10 | fmetafield | 元数据字段 | varchar | 2000 |  | √ | ' ' | 元数据字段 |
| 11 | fvisibility | 移动端可见性 | bpchar | 1 |  | √ | '1' | 移动端可见性 |
| 12 | fiscombined | 是否组合字段 | bpchar | 1 |  | √ | '0' | 是否组合字段 |
| 13 | fmdisplayname | 移动端显示名称 | varchar | 500 |  | √ | ' ' | 移动端显示名称 |
| 14 | fformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 15 | fisgroupfield | 是否分组字段 | bpchar | 1 |  | √ | '0' | 是否分组字段 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fgrouptype | 分组方式 | varchar | 50 |  | √ | ' ' | 分组方式,枚举: concat :拼接 average :平均 sum :汇总 max :最大值 min :最小值 count :计数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_osr_dispscheme_entry |  | fentryid |
| 2 | idx_osr_dispschemee |  | fmdisplayname,ffieldalias |

---

## 功能按钮配置分录-子表 t_osr_dispscheme_entryop

- **表名称：** 功能按钮配置分录-子表
- **表名：** t_osr_dispscheme_entryop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopdisplaylocation | 所属区域 | varchar | 50 |  | √ | ' ' | 所属区域,枚举: |
| 3 | fopisprint | 是否打印 | bpchar | 1 |  | √ | '0' | 是否打印 |
| 4 | fopfieldkey | 按钮标识 | varchar | 100 |  | √ | ' ' | 按钮标识 |
| 5 | fopvisibility | 可见性 | bpchar | 1 |  | √ | '1' | 可见性 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fprintpkid | 打印的单据主键ID标识 | varchar | 50 |  | √ | ' ' | 打印的单据主键ID标识 |
| 8 | fopfieldremark | 按钮备注 | varchar | 1000 |  | √ | ' ' | 按钮备注 |
| 9 | fopisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fopprinttplid | 打印模板 | int8 | 64 |  | √ | 0 | [维护打印模板 bos_manageprinttpl](../cts_files/bos_manageprinttpl.md) |
| 11 | fopdefvisibility | fopdefvisibility | bpchar | 1 |  | √ | '1' |  |
| 12 | fprintformid | 打印单据标识 | varchar | 50 |  | √ | ' ' | 打印单据标识 |
| 13 | fprinttype | 打印方式 | bpchar | 1 |  | √ | ' ' | 打印方式,枚举: A :本地打印 B :云打印 C :PDF预览打印 |
| 14 | fopfieldname | 按钮名称 | varchar | 500 |  | √ | ' ' | 按钮名称 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispscheme_entryop |  | fentryid |
| 2 | osr_dispscheme_entryop_idx_fid |  | fid |
| 3 | osr_dispscheme_entryop_idx |  | fseq,fopfieldname,fopfieldkey |

---

## 功能按钮配置分录-多语言表 t_osr_dispscheme_entryop_l

- **表名称：** 功能按钮配置分录-多语言表
- **表名：** t_osr_dispscheme_entryop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fopfieldname | 按钮名称 | varchar | 1500 |  | √ | ' ' | 按钮名称 |
| 2 | fopdisplaylname | fopdisplaylname | varchar | 1500 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fopfieldremark | 按钮备注 | varchar | 2000 |  | √ | ' ' | 按钮备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | osr_dispscheme_entryop_l_idx |  | fentryid,flocaleid |
| 2 | pk_t_osr_dispscheme_entryop_l |  | fpkid |
