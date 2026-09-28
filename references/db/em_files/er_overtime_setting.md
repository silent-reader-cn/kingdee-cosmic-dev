# 订单超期设置-er_overtime_setting

## 订单超期设置-多语言表 t_er_overtimesetting_l

- **表名称：** 订单超期设置-多语言表
- **表名：** t_er_overtimesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_overtimesetting_l_pkey |  | fpkid |
| 2 | idx_er_ovtmsetting_l_lcid |  | fid,flocaleid |

---

## 订单超期设置-主表 t_er_overtimesetting

- **表名称：** 订单超期设置-主表
- **表名：** t_er_overtimesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsubmit | 订单超期提交控制 | bpchar | 1 |  | √ | '0' | 订单超期提交控制 |
| 5 | fservicetype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 1 :酒店 2 :机票 3 :用车 6 :火车 |
| 6 | fremind | 订单超期提醒控制 | bpchar | 1 |  | √ | '0' | 订单超期提醒控制 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisp | 服务商(废弃) | varchar | 30 |  | √ | ' ' | 服务商(废弃),枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fserver | 服务商 | int8 | 64 |  | √ | 0 | [服务商设置 er_biz_info](../em_files/er_biz_info.md) |
| 13 | fsubmitday | 订单超期提交（天） | int8 | 64 |  | √ | 0 | 订单超期提交（天） |
| 14 | fremindday | 订单超期提醒（天） | int8 | 64 |  | √ | 0 | 订单超期提醒（天） |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_overtimesetting_pkey |  | fid |
| 2 | idx_er_ovtimsetting_sertyp |  | fisp,fservicetype |
