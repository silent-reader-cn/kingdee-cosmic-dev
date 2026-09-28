# 银行连接配置信息-aqap_connections_info

## 银行连接配置信息-多语言表 t_aqap_connections_info_l

- **表名称：** 银行连接配置信息-多语言表
- **表名：** t_aqap_connections_info_l

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
| 1 | pk_t_aqap_connections_info_l |  | fpkid |
| 2 | idx_aqap_connections_info_l_0 |  | fid,flocaleid |

---

## 银行连接配置信息-主表 t_aqap_connections_info

- **表名称：** 银行连接配置信息-主表
- **表名：** t_aqap_connections_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | 银行启用管理 aqap_bank |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffile_ip | 文件服务地址 | varchar | 255 |  | √ | ' ' | 文件服务地址 |
| 8 | fip | 服务网关地址 | varchar | 255 |  | √ | ' ' | 服务网关地址 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprotocol | 通讯协议 | varchar | 50 |  | √ | ' ' | 通讯协议,枚举: HTTP :HTTP HTTPS :HTTPS TCP :TCP UDP :UDP |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ffile_port | 文件端口 | int8 | 64 |  | √ | 0 | 文件端口 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 环境类型 | varchar | 50 |  | √ | ' ' | 环境类型,枚举: prod :生产环境 test :测试环境 |
| 16 | fport | 端口号 | int8 | 64 |  | √ | 0 | 端口号 |
| 17 | furi | URI路径 | varchar | 255 |  | √ | ' ' | URI路径 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | ffile_uri | 文件URI路径 | varchar | 255 |  | √ | ' ' | 文件URI路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_connections_info |  | fid |
| 2 | idx_aqap_connections_info_0 |  | fgroupid |
