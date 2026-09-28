# 工作日历-tbd_workcalendar

## 单据体-子表 t_tbd_workcalendar_entrys

- **表名称：** 单据体-子表
- **表名：** t_tbd_workcalendar_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | varchar | 30 |  | √ | ' ' | 日期类型,枚举: |
| 3 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fworkdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_workcalendar_entrys |  | fentryid |
| 2 | idx_tbd_workcalendar_entrys_id |  | fid,fentryid |

---

## 工作日历-主表 t_tbd_workcalendar

- **表名称：** 工作日历-主表
- **表名：** t_tbd_workcalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 3 | fminofendtimeam | 上午结束分 | varchar | 30 |  | √ | ' ' | 上午结束分,枚举: 0 :00 5 :05 10 :10 15 :15 20 :20 25 :25 30 :30 35 :35 40 :40 45 :45 50 :50 55 :55 |
| 4 | fiswedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 5 | fishalfmonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 6 | fminofbegintimeam | 上午开始分 | varchar | 30 |  | √ | ' ' | 上午开始分,枚举: 0 :00 5 :05 10 :10 15 :15 20 :20 25 :25 30 :30 35 :35 40 :40 45 :45 50 :50 55 :55 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fishalftuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 9 | fishalfsatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fishalfwedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 14 | fhourofendtimepm | 下午结束小时 | varchar | 30 |  | √ | ' ' | 下午结束小时,枚举: 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 |
| 15 | fisfrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 16 | fexpiremonthto | 结束月 | varchar | 30 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 17 | fishalfthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 18 | fismonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 19 | fhourofendtimeam | 上午结束小时 | varchar | 30 |  | √ | ' ' | 上午结束小时,枚举: 0 :00 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 20 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fminofbegintimepm | 下午开始分 | varchar | 30 |  | √ | ' ' | 下午开始分,枚举: 0 :00 5 :05 10 :10 15 :15 20 :20 25 :25 30 :30 35 :35 40 :40 45 :45 50 :50 55 :55 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fhourofbegintimeam | 工作日上午 | varchar | 30 |  | √ | ' ' | 工作日上午,枚举: 0 :00 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 25 | fisthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 26 | fissatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 27 | fishalfsunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 28 | fexpiremonthfrom | 开始月 | varchar | 30 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 29 | fistuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 30 | fishalffrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 31 | fminofendtimepm | 下午结束分 | varchar | 30 |  | √ | ' ' | 下午结束分,枚举: 0 :00 5 :05 10 :10 15 :15 20 :20 25 :25 30 :30 35 :35 40 :40 45 :45 50 :50 55 :55 |
| 32 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 33 | fexpireyearto | 结束年 | varchar | 30 |  | √ | ' ' | 结束年,枚举: |
| 34 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 35 | fhourofbegintimepm | 工作日下午 | varchar | 30 |  | √ | ' ' | 工作日下午,枚举: 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 |
| 36 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 37 | fexpireyearfrom | 有效期间 | varchar | 30 |  | √ | ' ' | 有效期间,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_work_bb |  | fnumber |
| 2 | pk_t_tbd_workcalendar |  | fid |

---

## 工作日历-多语言表 t_tbd_workcalendar_l

- **表名称：** 工作日历-多语言表
- **表名：** t_tbd_workcalendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_workcalendar_l_id |  | fid,flocaleid |
| 2 | pk_t_tbd_workcalendar_l |  | fpkid |
