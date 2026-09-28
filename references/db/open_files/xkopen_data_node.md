# 数据节点-xkopen_data_node

## 数据节点-多语言表 t_xkopen_initialdata_l

- **表名称：** 数据节点-多语言表
- **表名：** t_xkopen_initialdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkopen_initialdata_l |  | fpkid |
| 2 | idx_xkopen_initialdata_l_fid |  | fid,flocaleid |

---

## 数据节点-主表 t_xkopen_initialdata

- **表名称：** 数据节点-主表
- **表名：** t_xkopen_initialdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreapp_status | 预置应用同步启用状态 | varchar | 10 |  | √ | ' ' | 预置应用同步启用状态 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fresourceupdate_status | 资源更新计划 | varchar | 10 |  | √ | ' ' | 资源更新计划 |
| 6 | fapinum_status | API数目扫描状态 | varchar | 10 |  | √ | ' ' | API数目扫描状态 |
| 7 | fapisyn_status | API同步状态 | varchar | 10 |  | √ | ' ' | API同步状态 |
| 8 | fstart_status | 启动增量计划状态 | varchar | 10 |  | √ | ' ' | 启动增量计划状态 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fapp_num | 预置应用数量 | int8 | 64 |  | √ | 0 | 预置应用数量 |
| 11 | flog_printing | 日志打印 | varchar | 2000 |  | √ | ' ' | 日志打印 |
| 12 | fhomepage_box | 首页弹框是否关闭 | varchar | 10 |  | √ | ' ' | 首页弹框是否关闭 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fpageplay_status | 当前页面展示。 | varchar | 10 |  | √ | ' ' | 当前页面展示。 |
| 15 | fsecretkey_status | 秘钥申请状态 | varchar | 10 |  | √ | ' ' | 秘钥申请状态 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fresourceupdate_time | 初始化完成时间 | varchar | 50 |  | √ | ' ' | 初始化完成时间 |
| 21 | fappsyn_status | 预置应用同步状态 | varchar | 10 |  | √ | ' ' | 预置应用同步状态 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fapi_num | API数量 | int8 | 64 |  | √ | 0 | API数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkopen_initialdata |  | fid |
