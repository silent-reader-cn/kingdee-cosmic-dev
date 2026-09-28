# 资金计划模板备份表（废弃）-fpm_template_bak

## 科目成员-子表 t_fpm_templatebak_subject

- **表名称：** 科目成员-子表
- **表名：** t_fpm_templatebak_subject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisleaf | 是否为叶子节点 | bpchar | 1 |  | √ | '1' | 是否为叶子节点 |
| 3 | freportways | 编报方式 | varchar | 50 |  | √ | ' ' | 编报方式,枚举: 0 :手工录入 1 :公式项 2 :汇总项 3 :明细填报 |
| 4 | fformula | 适用公式 | varchar | 1000 |  | √ | ' ' | 适用公式 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fformula_tag | 适用公式_详情 | text | 0 |  |  | null | 适用公式_详情 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsubjectid | 科目 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 9 | fsubtemplateid | 子模板 | int8 | 64 |  | √ | 0 | [资金计划模板备份表（废弃） fpm_template_bak](../fpm_files/fpm_template_bak.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_templatebak_subject |  | fid |
| 2 | pk_t_fpm_templatebak_subject |  | fentryid |

---

## 科目-多选基础资料表 t_fpm_tplbak_subjectme

- **表名称：** 科目-多选基础资料表
- **表名：** t_fpm_tplbak_subjectme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_tplbak_subjectme |  | fid |
| 2 | pk_t_fpm_tplbak_subjectme |  | fpkid |

---

## 资金计划模板备份表（废弃）-主表 t_fpm_templateinfo_bak

- **表名称：** 资金计划模板备份表（废弃）-主表
- **表名：** t_fpm_templateinfo_bak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstartcell | 报表起始单元格 | varchar | 50 |  | √ | ' ' | 报表起始单元格 |
| 3 | fmaxnum | 明细模板最大行数 | int4 | 32 |  | √ | 0 | 明细模板最大行数 |
| 4 | famountunit | 金额单位 | varchar | 50 |  | √ | ' ' | 金额单位,枚举: one :元 thousand :千元 ten_thousand :万元 million :百万元 hundred_million :亿元 fromparent :沿用主表 |
| 5 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | ftemplatetype | 模板类型 | varchar | 50 |  | √ | ' ' | 模板类型,枚举: FIX :固定模板 DET :明细模板 |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fisincludesum | 明细模板是否包含合计行 | bpchar | 1 |  | √ | '0' | 明细模板是否包含合计行 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fspreaddata | spread序列化信息 | varchar | 500 |  | √ | ' ' | spread序列化信息 |
| 15 | fismaintable | 是否为主表 | bpchar | 1 |  | √ | '0' | 是否为主表 |
| 16 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftemplateid | 源模板 | int8 | 64 |  | √ | 0 | 源模板 |
| 18 | fsubtemplatecount | 关联子模板数量 | int4 | 32 |  | √ | 0 | 关联子模板数量 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fisshowcombine | 是否显示合计列 | bpchar | 1 |  | √ | '0' | 是否显示合计列 |
| 21 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 22 | freleasestatus | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态 |
| 23 | fisshownote | 是否显示备注列 | bpchar | 1 |  | √ | '0' | 是否显示备注列 |
| 24 | fsmartgetvalset | 智能编制取值设置 | varchar | 50 |  | √ | 'fillplanamt' | 智能编制取值设置,枚举: fillplanamt :直接填充计划数 referenceval :单列计划填报参考值 |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fnotename | 备注列名称 | varchar | 100 |  | √ | ' ' | 备注列名称 |
| 27 | fspreaddata_tag | spread序列化信息_详情 | text | 0 |  |  | null | spread序列化信息_详情 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fisdistinguish | 是否区分列维成员 | bpchar | 1 |  | √ | '0' | 是否区分列维成员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_templateinfo_bak |  | fid |
| 2 | idx_t_fpm_templateinfo_bak |  | fnumber |

---

## 成员范围-多选基础资料表 t_fpm_tplbak_member

- **表名称：** 成员范围-多选基础资料表
- **表名：** t_fpm_tplbak_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_tplbak_member |  | fid |
| 2 | pk_t_fpm_tplbak_member |  | fpkid |

---

## 资金计划模板备份表（废弃）-多语言表 t_fpm_templateinfo_bak_l

- **表名称：** 资金计划模板备份表（废弃）-多语言表
- **表名：** t_fpm_templateinfo_bak_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_templateinfo_bak_l |  | fpkid |
| 2 | idx_t_fpm_templateinfo_bak_l |  | fid |

---

## 适用组织-多选基础资料表 t_fpm_templatebakuser

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_fpm_templatebakuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_templatebakuser |  | fid |
| 2 | pk_t_fpm_templatebakuser |  | fpkid |

---

## 适用编报类型-多选基础资料表 t_fpm_tplbak_reporttype

- **表名称：** 适用编报类型-多选基础资料表
- **表名：** t_fpm_tplbak_reporttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_tplbak_reporttype |  | fpkid |
| 2 | idx_t_fpm_tplbak_reporttype |  | fid |

---

## 单据体-子表 t_fpm_tplbak_retypeentry

- **表名称：** 单据体-子表
- **表名：** t_fpm_tplbak_retypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frefrenceorg | 期间参考来源 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 3 | frefrenceposition | 参考指标 | varchar | 50 |  | √ | ' ' | 参考指标,枚举: planamt :计划数 actmat :执行数 banlance :执行差额 avliablebanlance :可用余额 |
| 4 | fperiodnum | 期数 | int4 | 32 |  | √ | 0 | 期数 |
| 5 | freporttype | 编报期间 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_tplbak_rte_fid |  | fid |
| 2 | pk_t_fpm_tplbak_retypeentry |  | fentryid |

---

## 单据体-子表 t_fpm_templatebak_layout

- **表名称：** 单据体-子表
- **表名：** t_fpm_templatebak_layout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimhide | 是否隐藏 | bpchar | 1 |  | √ | '0' | 是否隐藏 |
| 3 | fdimtype | 维度布局 | varchar | 50 |  | √ | ' ' | 维度布局,枚举: row :行维 col :列维 page :页面维 |
| 4 | fisexpandmem | 是否按成员平铺展开 | bpchar | 1 |  | √ | '0' | 是否按成员平铺展开 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fiscontaintotal | 是否包含小计 | bpchar | 1 |  | √ | '0' | 是否包含小计 |
| 7 | fdimlevel | 行列维级别 | varchar | 50 |  | √ | ' ' | 行列维级别,枚举: 1 :一级 2 :二级 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | flayoutdim | 维度 | int8 | 64 |  | √ | 0 | [维度（废弃） fpm_dimension](../fpm_files/fpm_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_templatebak_layout |  | fid |
| 2 | pk_t_fpm_templatebak_layout |  | fentryid |

---

## 行列维设置-子表 t_fpm_templatebak_dimset

- **表名称：** 行列维设置-子表
- **表名：** t_fpm_templatebak_dimset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fisopen | 是否平铺展开 | bpchar | 1 |  | √ | '0' | 是否平铺展开 |
| 4 | fdimbdtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: fpm_dimension :维度 fpm_detailplanfields :明细计划字段 |
| 5 | flevel | 行列维级别 | int4 | 32 |  | √ | 0 | 行列维级别 |
| 6 | ftype | 行列类型 | varchar | 50 |  | √ | ' ' | 行列类型,枚举: row :行 col :列 page :页面 |
| 7 | fsequence | 行列维序号 | int4 | 32 |  | √ | 0 | 行列维序号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdimid | 维度ID | int8 | 64 |  | √ | 0 | 维度ID |
| 10 | fcontainsubtotal | 是否包含小计 | bpchar | 1 |  | √ | '0' | 是否包含小计 |
| 11 | fdimbdid | 维度 | int8 | 64 |  | √ | 0 | 维度（废弃） fpm_dimension |
| 12 | fishide | 是否隐藏 | bpchar | 1 |  | √ | '0' | 是否隐藏 |
| 13 | fisdetaildim | 是否为明细维度 | bpchar | 1 |  | √ | '0' | 是否为明细维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_templatebak_dimset |  | fentryid |
| 2 | idx_t_fpm_templatebak_dimset |  | fid |

---

## 单据体-子表 t_fpm_tplbak_metric

- **表名称：** 单据体-子表
- **表名：** t_fpm_tplbak_metric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 3 | fbizfiled | 业务字段 | varchar | 50 |  | √ | ' ' | 业务字段,枚举: |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmetrictype | 度量值类型 | varchar | 50 |  | √ | ' ' | 度量值类型,枚举: |
| 6 | freturnval | 是否可回写 | bpchar | 1 |  | √ | '0' | 是否可回写 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_tplbak_metric |  | fentryid |
| 2 | idx_t_fpm_tplbak_metric_fid |  | fid |

---

## 展开成员-多选基础资料表 t_fpm_tplbak_layoutmem

- **表名称：** 展开成员-多选基础资料表
- **表名：** t_fpm_tplbak_layoutmem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_tplbak_layoutmem |  | fid |
| 2 | pk_t_fpm_tplbak_layoutmem |  | fpkid |

---

## 币别-多选基础资料表 t_fpm_tplbak_currency

- **表名称：** 币别-多选基础资料表
- **表名：** t_fpm_tplbak_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_tplbak_currency |  | fpkid |
| 2 | idx_t_fpm_tplbak_currency |  | fid |
