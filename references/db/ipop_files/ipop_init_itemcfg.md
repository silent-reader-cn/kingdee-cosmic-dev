# 初始化事项配置-ipop_init_itemcfg

## 初始化事项配置-多语言表 t_ipop_init_itemcfg_l

- **表名称：** 初始化事项配置-多语言表
- **表名：** t_ipop_init_itemcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_itemcfg_l |  | fpkid |
| 2 | idx_ipop_init_itemcfg_l |  | fid,flocaleid |

---

## 单据体-子表 t_ipop_init_itemcfgentry

- **表名称：** 单据体-子表
- **表名：** t_ipop_init_itemcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizitemid | 业务初始化子项 | int8 | 64 |  | √ | 0 | 指引步骤关联页面/表单 xkguide_ref |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_itemcfgentry |  | fentryid |
| 2 | idx_ipop_init_itemcfgentry_id |  | fid |

---

## 初始化事项配置-主表 t_ipop_init_itemcfg

- **表名称：** 初始化事项配置-主表
- **表名：** t_ipop_init_itemcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmenuparam | 菜单参数 | varchar | 200 |  | √ | ' ' | 菜单参数 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fknowledgeurl | 社区知识地址 | varchar | 200 |  | √ | ' ' | 社区知识地址 |
| 6 | fappnumber | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 7 | findex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fshowbymultiorg | 是否仅多组织显示 | bpchar | 1 |  | √ | ' ' | 是否仅多组织显示 |
| 10 | fmoduleid | 初始化模块 | int8 | 64 |  | √ | 0 | 初始化模块配置 ipop_init_modulecfg |
| 11 | finitdatainput | 纳入期初数据统计 | bpchar | 1 |  | √ | ' ' | 纳入期初数据统计 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdefault | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fshowbyorg | 是否按组织显示 | bpchar | 1 |  | √ | ' ' | 是否按组织显示 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fhasexceltpl | 支持下载模板 | bpchar | 1 |  | √ | ' ' | 支持下载模板 |
| 21 | fformid | 业务对象编码 | varchar | 100 |  | √ | ' ' | 业务对象编码 |
| 22 | fmenuid | 菜单ID | varchar | 50 |  | √ | ' ' | 菜单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_itemcfg |  | fid |
| 2 | idx_ipop_init_itemcfg_num |  | fnumber |
| 3 | idx_ipop_init_itemcfg_mod |  | fmoduleid |
