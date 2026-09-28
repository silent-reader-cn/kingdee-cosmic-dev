# 合规管控方案-src_conformscheme

## 招标流程-多选基础资料表 t_src_conformflow

- **表名称：** 招标流程-多选基础资料表
- **表名：** t_src_conformflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_conformflow |  | fpkid |
| 2 | idx_src_conformflow_bid |  | fbasedataid |
| 3 | idx_src_conformflow_fid |  | fid |

---

## 参数分录-子表 t_src_conformparams

- **表名称：** 参数分录-子表
- **表名：** t_src_conformparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 参数值 | varchar | 512 |  | √ | ' ' | 参数值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 4 | fbasedatainfo | 参数说明 | varchar | 512 |  | √ | ' ' | 参数说明 |
| 5 | fismustinput | 是否必录 | bpchar | 1 |  | √ | ' ' | 是否必录 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_conformparams |  | fentryid |
| 2 | idx_src_conformparams_fid |  | fid |

---

## 检查项分录-子表 t_src_conformentry

- **表名称：** 检查项分录-子表
- **表名：** t_src_conformentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompobjid | 检查结果组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 3 | fcontroltype | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 0 :不控制 1 :提醒 2 :禁止 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 6 | fdescription | 检查内容描述 | varchar | 255 |  | √ | ' ' | 检查内容描述 |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 8 | flogtype | 日志记录方式 | bpchar | 1 |  | √ | ' ' | 日志记录方式,枚举: 1 :记录异常明细 2 :记录所有明细 3 :不记录明细 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpluginname | 插件 | varchar | 100 |  | √ | ' ' | 插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_conformentry |  | fentryid |
| 2 | idx_src_conformentry_fid |  | fid |

---

## 采购组织-多选基础资料表 t_src_conformpurorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_conformpurorg

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
| 1 | idx_src_conformpurorg_bid |  | fbasedataid |
| 2 | idx_src_conformpurorg_fid |  | fid |
| 3 | pk_src_conformpurorg |  | fpkid |

---

## 业务类型-多选基础资料表 t_src_conformbiztype

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_src_conformbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_conformbiztype |  | fpkid |
| 2 | idx_src_conformbiztype_fid |  | fid |
| 3 | idx_src_conformbiztype_bid |  | fbasedataid |

---

## 合规管控方案-主表 t_src_conformscheme

- **表名称：** 合规管控方案-主表
- **表名：** t_src_conformscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbizobject | 业务对象 | varchar | 30 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 8 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | foperation | 业务操作 | varchar | 30 |  | √ | ' ' | 业务操作,枚举: submit :提交 allopen :开标 tecopen :开技术标 bizopen :开商务标 aptopen :开资审标 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_conformscheme_num |  | fnumber |
| 2 | idx_src_conformscheme_obj_op |  | fbizobject,foperation |
| 3 | pk_src_conformscheme |  | fid |

---

## 合规管控方案-多语言表 t_src_conformscheme_l

- **表名称：** 合规管控方案-多语言表
- **表名：** t_src_conformscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_conformscheme_l_id |  | fid,flocaleid |
| 2 | pk_src_conformscheme_l |  | fpkid |

---

## 招标方式-多选基础资料表 t_src_conformtype

- **表名称：** 招标方式-多选基础资料表
- **表名：** t_src_conformtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_conformtype_bid |  | fbasedataid |
| 2 | pk_src_conformtype |  | fpkid |
| 3 | idx_src_conformtype_fid |  | fid |
