# 产品树追溯路径-pqt_retraceroute

## 产品树追溯路径-使用范围表 t_pqt_retraceroute_u

- **表名称：** 产品树追溯路径-使用范围表
- **表名：** t_pqt_retraceroute_u

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
| 1 | pk_t_pqt_retraceroute_u |  | fdataid,fuseorgid |
| 2 | idx_t_pqt_retraceroute_u_uo |  | fuseorgid |

---

## 追溯路径-子表 t_pqt_routeentry

- **表名称：** 追溯路径-子表
- **表名：** t_pqt_routeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisrountbegin | 路径起点 | bpchar | 1 |  | √ | '0' | 路径起点 |
| 3 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 4 | ftracelogic | 单据追溯逻辑 | int8 | 64 |  | √ | 0 | 单据追溯逻辑 pqt_billretracelogic |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdescription | 描述说明 | varchar | 255 |  | √ | ' ' | 描述说明 |
| 7 | fisrountend | 路径终点 | bpchar | 1 |  | √ | '0' | 路径终点 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | froutnumber | 路径编号 | int4 | 32 |  | √ | 0 | 路径编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pqt_routeentry_fseq |  | fseq |
| 2 | pk_t_pqt_routeentry |  | fentryid |
| 3 | idx_pqt_routeentry_fid |  | fid |

---

## 产品树追溯路径-主表 t_pqt_retraceroute

- **表名称：** 产品树追溯路径-主表
- **表名：** t_pqt_retraceroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 10 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 11 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ftracedirection | 追溯方向 | varchar | 10 |  | √ | ' ' | 追溯方向,枚举: TW_GO :去向追溯 TW_BACK :溯源追溯 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 21 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fsystempreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pqt_retraceroute_master |  | fmasterid |
| 2 | idx_t_pqt_retraceroute_createorg |  | fcreateorgid |
| 3 | pk_t_pqt_retraceroute |  | fid |
| 4 | idx_pqt_retraceroute_fnumber |  | fnumber |

---

## 产品树追溯路径-多语言表 t_pqt_retraceroute_l

- **表名称：** 产品树追溯路径-多语言表
- **表名：** t_pqt_retraceroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pqt_retraceroute_fid |  | fid,flocaleid |
| 2 | pk_t_pqt_retraceroute_l |  | fpkid |
