# 许可使用-rpap_isrpa_license_bind

## 许可使用-主表 t_rpap_isrpa_license_bind

- **表名称：** 许可使用-主表
- **表名：** t_rpap_isrpa_license_bind

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterminaltype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 0 :机器人 1 :设计器 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | frpausername | 登录rpa机器人的rpa账号 | varchar | 50 |  | √ | ' ' | 登录rpa机器人的rpa账号 |
| 7 | foperatesysuser | 操作系统用户名 | varchar | 50 |  | √ | ' ' | 操作系统用户名 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fuserorgname | 用户组织 | varchar | 255 |  | √ | ' ' | 用户组织 |
| 11 | foperatesys | 操作系统 | varchar | 50 |  | √ | ' ' | 操作系统 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | flicense | 许可信息 | int8 | 64 |  | √ | 0 | 许可 rpap_isrpa_license |
| 15 | fagentdcode | 机器码 | varchar | 50 |  | √ | ' ' | 机器码 |
| 16 | fcustomid | 客户端id | varchar | 50 |  | √ | ' ' | 客户端id |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fagentno | 机器人终端编号 | varchar | 50 |  | √ | ' ' | 机器人终端编号 |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | frunningstate | 运行状态 | varchar | 30 |  | √ | ' ' | 运行状态,枚举: 0 :离线 1 :在线 |
| 21 | fhostname | 计算机名 | varchar | 255 |  | √ | ' ' | 计算机名 |
| 22 | frbname | 别名 | varchar | 255 |  | √ | ' ' | 别名 |
| 23 | fipaddr | ip地址 | varchar | 255 |  | √ | ' ' | ip地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_isrpa_license_bind |  | fid |
| 2 | idx_isrpa_license_bind_num |  | fnumber |

---

## 许可使用-多语言表 t_rpap_isrpa_license_bind_l

- **表名称：** 许可使用-多语言表
- **表名：** t_rpap_isrpa_license_bind_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_isrpa_license_bind_l |  | fpkid |
| 2 | idx_isrpa_license_bind_l |  | fid |
