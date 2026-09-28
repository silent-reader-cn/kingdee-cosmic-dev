# 标书文件过滤-pds_docfilter

## 标书文件过滤-多语言表 t_pds_docfilter_l

- **表名称：** 标书文件过滤-多语言表
- **表名：** t_pds_docfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_docfilter_l_fid |  | fid |
| 2 | idx_pds_docfilter_l_fname |  | fname |
| 3 | pk_pds_docfilter_l |  | fpkid |

---

## 招标流程-多选基础资料表 t_pds_docfilter_srcflow

- **表名称：** 招标流程-多选基础资料表
- **表名：** t_pds_docfilter_srcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_docfilter_srcflow |  | fpkid |
| 2 | idx_pds_docfilter_srcflow_fid |  | fid |
| 3 | idx_pds_docfilter_srcflow_bid |  | fbasedataid |

---

## 标书文件过滤-主表 t_pds_docfilter

- **表名称：** 标书文件过滤-主表
- **表名：** t_pds_docfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fbasetype | 评分类型 | bpchar | 1 |  | √ | ' ' | 评分类型,枚举: 1 :评技术标 2 :评商务标 3 :评商务综合 4 :资质预审 7 :资质后审 6 :综合评标(技术+商务+商务综合) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fisopencontrol | 仅查看已开标的文件 | bpchar | 1 |  | √ | '1' | 仅查看已开标的文件 |
| 10 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fopentype | 开标方式 | varchar | 50 |  | √ | ' ' | 开标方式,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 3 :自动开标 4 :并行开技术标和商务标 9 :报价即开标(非密封报价) |
| 15 | fpackfiletype | 可查看的文件类型 | varchar | 50 |  | √ | ' ' | 可查看的文件类型,枚举: 1 :技术标书 2 :商务标书 3 :通用标书 4 :商务综合标书 5 :资审审查标书 6 :报名附件 7 :协同附件 8 :报价附件 |
| 16 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fopenstatus | 当前项目的开标状态 | varchar | 50 |  | √ | ' ' | 当前项目的开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 6 :议价中 9 :已定标 A :已归档 B :已终止 |
| 19 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fbiznode | 业务节点/业务对象 | varchar | 30 |  | √ | ' ' | 业务对象 bos_objecttype |
| 21 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_docfilter_fnumber |  | fnumber |
| 2 | pk_pds_docfilter |  | fid |
| 3 | idx_pds_docfilter_fbid |  | fbiznode |
| 4 | idx_pds_docfilter_fmasterid |  | fmasterid |

---

## 寻源方式-多选基础资料表 t_pds_docfilter_srctype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_pds_docfilter_srctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_docfilter_srctype_bid |  | fbasedataid |
| 2 | pk_pds_docfilter_srctype |  | fpkid |
| 3 | idx_pds_docfilter_srctype_fid |  | fid |

---

## 当前用户的业务角色-多选基础资料表 t_pds_docfilter_bizrole

- **表名称：** 当前用户的业务角色-多选基础资料表
- **表名：** t_pds_docfilter_bizrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_docfilter_bizrole_bid |  | fbasedataid |
| 2 | idx_pds_docfilter_bizrole_fid |  | fid |
| 3 | pk_pds_docfilter_bizrole |  | fpkid |
