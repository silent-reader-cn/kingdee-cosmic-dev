# 行程管控设置-er_tripcontrolsettings

## 行程管控设置-多语言表 t_er_tripcontrol_l

- **表名称：** 行程管控设置-多语言表
- **表名：** t_er_tripcontrol_l

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
| 1 | idx_er_tripctrl_fid |  | fid,flocaleid |
| 2 | t_er_tripcontrol_l_pkey |  | fpkid |

---

## 行程管控设置-使用范围位图表 t_er_tripcontrol_m

- **表名称：** 行程管控设置-使用范围位图表
- **表名：** t_er_tripcontrol_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripcontrol_m |  | forgid |

---

## 行程管控设置-使用范围表 t_er_tripcontrol_u

- **表名称：** 行程管控设置-使用范围表
- **表名：** t_er_tripcontrol_u

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
| 1 | idx_t_er_tripcontrol_u_uo |  | fuseorgid |
| 2 | t_er_tripcontrol_u_pkey |  | fdataid,fuseorgid |

---

## 行程管控设置-主表 t_er_tripcontrol

- **表名称：** 行程管控设置-主表
- **表名：** t_er_tripcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhotelcityctrl | 城市管控 | varchar | 5 |  | √ | ' ' | 城市管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 3 | fendcityrule | 行程终点是否包含市内用车权限 | varchar | 5 |  | √ | '2' | 行程终点是否包含市内用车权限,枚举: 0 :否 1 :是 |
| 4 | fdomairdiscountctrl | 折扣 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fstartcityrule | 行程起点是否包含市内用车权限 | varchar | 5 |  | √ | '2' | 行程起点是否包含市内用车权限,枚举: 0 :否 1 :是 |
| 7 | fdomairbookcountctrl | 预订次数管控 | int8 | 64 |  | √ | 0 | 预订次数管控 |
| 8 | fdomaircityctrl | 城市管控 | varchar | 5 |  | √ | ' ' | 城市管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fhotelbookcountctrl | 预订次数管控 | int8 | 64 |  | √ | 0 | 预订次数管控 |
| 12 | fintlairroundtripctrl | 单程/往返管控 | varchar | 5 |  | √ | ' ' | 单程/往返管控,枚举: 1 :允许预订单程 2 :允许预订往返 |
| 13 | fdayroomcount | 每日房间数量 | int8 | 64 |  | √ | 0 | 每日房间数量 |
| 14 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fintlairbookcountctrl | 预订次数管控 | int8 | 64 |  | √ | 0 | 预订次数管控 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fserver | 商旅服务商 | varchar | 30 |  | √ | ' ' | 商旅服务商,枚举: ZHONGXING :中兴e路通 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 |
| 19 | fdomairtrippeoplectrl | 出行人管控 | varchar | 5 |  | √ | ' ' | 出行人管控,枚举: 2 :不控制 0 :按出行人姓名管控 1 :按出行人工号管控 |
| 20 | fcarcityctrl | 城市管控 | varchar | 5 |  | √ | ' ' | 城市管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 21 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 22 | fcartrippeoplectrl | 出行人管控 | varchar | 5 |  | √ | ' ' | 出行人管控,枚举: 2 :不控制 0 :按出行人姓名管控 1 :按出行人工号管控 |
| 23 | fintlairdiscountctrl | 折扣 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣 |
| 24 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 25 | fdomairroundtripctrl | 单程/往返管控 | varchar | 5 |  | √ | ' ' | 单程/往返管控,枚举: 1 :允许预订单程 2 :允许预订往返 |
| 26 | fhoteldatectrl | 日期管控 | varchar | 5 |  | √ | ' ' | 日期管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 27 | fintlairdatectrl | 日期管控 | varchar | 5 |  | √ | ' ' | 日期管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 28 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fcarbookcountctrl | 预订次数管控 | int8 | 64 |  | √ | 0 | 预订次数管控 |
| 31 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 32 | fdomairdatectrl | 日期管控 | varchar | 5 |  | √ | ' ' | 日期管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 33 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 34 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 35 | fcardatectrl | 日期管控 | varchar | 5 |  | √ | ' ' | 日期管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 36 | fmixstarclass | 最小星级 | int8 | 64 |  | √ | 0 | 最小星级 |
| 37 | fmaxstarclass | 最大星级 | int8 | 64 |  | √ | 0 | 最大星级 |
| 38 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fhoteltrippeoplectrl | 出行人管控 | varchar | 5 |  | √ | ' ' | 出行人管控,枚举: 2 :不控制 0 :按出行人姓名管控 1 :按出行人工号管控 |
| 40 | fintlairtrippeoplectrl | fintlairtrippeoplectrl | varchar | 5 |  | √ | ' ' |  |
| 41 | fintlaircityctrl | 城市管控 | varchar | 5 |  | √ | ' ' | 城市管控,枚举: 0 :不控制 1 :按行程控制 2 :按整单控制 |
| 42 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 43 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_tripcs_server |  | fserver |
| 2 | idx_t_er_tripcontrol_createorg |  | fcreateorgid |
| 3 | t_er_tripcontrol_pkey |  | fid |
| 4 | idx_t_er_tripcontrol_master |  | fmasterid |
| 5 | index_er_tripcs_creatorg |  | fcreateorgid |
