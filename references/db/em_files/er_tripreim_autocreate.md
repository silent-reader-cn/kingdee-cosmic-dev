# 自动差旅报销-er_tripreim_autocreate

## 自动差旅报销-主表 t_er_tripreim_autocreate

- **表名称：** 自动差旅报销-主表
- **表名：** t_er_tripreim_autocreate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillcreator | 单据创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpushmode | 报销方式 | bpchar | 1 |  | √ | '0' | 报销方式,枚举: 0 :不生成单据 1 :生成单据\|(暂存) 2 :生成单据并提交 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftarbilltype | 目标单 | varchar | 50 |  | √ | ' ' | 目标单,枚举: er_tripreimbursebill :差旅报销单 |
| 7 | fuserdefinerule | 自定义条件json | varchar | 2000 |  | √ | ' ' | 自定义条件json |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpushperson | 消息推送对象 | varchar | 30 |  | √ | ' ' | 消息推送对象,枚举: creator :制单人 applier :申请人 travelers :出差人 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fudrdisplay | 自定义条件： | varchar | 2000 |  | √ | ' ' | 自定义条件： |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 19 | fpushtime | 报销时点（天） | int8 | 64 |  | √ | 0 | 报销时点（天） |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fautomaticmatch | Cosmic匹配费用项目 | bpchar | 1 |  | √ | '0' | Cosmic匹配费用项目 |
| 22 | fjs | js文本 | varchar | 2000 |  | √ | ' ' | js文本 |
| 23 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | freimscope | 报销范围 | bpchar | 1 |  | √ | '0' | 报销范围,枚举: 0 :全部差旅项目 1 :商旅订单与补助 2 :仅商旅订单 |
| 25 | fonlylinkedorder | 关联商旅订单 | bpchar | 1 |  | √ | '0' | 关联商旅订单 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 28 | fsrcbilltype | 源单 | varchar | 50 |  | √ | ' ' | 源单,枚举: er_tripreqbill :出差申请单 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_tripreim_autocreate |  | fid |
| 2 | idx_t_er_tripreim_autocreate_createorg |  | fcreateorgid |
| 3 | idx_t_er_tripreim_autocreate_master |  | fmasterid |
| 4 | idx_t_er_tripreim_autocreate |  | fmasterid |

---

## 自动差旅报销-使用范围表 t_er_tripreim_autocreate_u

- **表名称：** 自动差旅报销-使用范围表
- **表名：** t_er_tripreim_autocreate_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_tripreim_autocreate_u_uo |  | fuseorgid |
| 2 | pk_t_er_tripreim_autocreate_u |  | fdataid,fuseorgid |

---

## 自动差旅报销-多语言表 t_er_tripreim_autocreate_l

- **表名称：** 自动差旅报销-多语言表
- **表名：** t_er_tripreim_autocreate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_tripreim_autocreate_l |  | fpkid |
| 2 | idx_er_tripreim_autocreate_l |  | fid,flocaleid |
