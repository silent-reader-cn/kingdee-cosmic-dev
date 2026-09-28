# 文件操作日志-bos_attachment_oplog

## 文件操作日志-多语言表 t_bas_attachment_oplog_l

- **表名称：** 文件操作日志-多语言表
- **表名：** t_bas_attachment_oplog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 操作描述 | varchar | 500 |  | √ | ' ' | 操作描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_attachment_oplog_l_0 |  | fid,flocaleid |
| 2 | pk_bas_attachment_oplog_l |  | fpkid |

---

## 文件操作日志-主表 t_bas_attachment_oplog

- **表名称：** 文件操作日志-主表
- **表名：** t_bas_attachment_oplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjname | 操作对象名 | varchar | 128 |  | √ | ' ' | 操作对象名 |
| 3 | fentitynum | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | ffilelocation | 文件位置 | bpchar | 1 |  | √ | '1' | 文件位置,枚举: 0 :临时文件服务器 1 :文件服务器 2 :未上传服务器 |
| 5 | forgid | 操作组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foptype | 操作类型 | bpchar | 1 |  | √ | '0' | 操作类型,枚举: 0 :保存 1 :上传 2 :预览 3 :下载 4 :删除 5 :备注 6 :重命名 |
| 7 | fatttype | 附件分类（附件面板/附件字段） | bpchar | 1 |  | √ | '0' | 附件分类（附件面板/附件字段） |
| 8 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 操作描述 | varchar | 500 |  | √ | ' ' | 操作描述 |
| 10 | fattpkid | 附件表PKID | int8 | 64 |  | √ | 0 | 附件表PKID |
| 11 | fclientip | 客户端地址 | varchar | 128 |  | √ | ' ' | 客户端地址 |
| 12 | fusername | 操作用户名 | varchar | 128 |  | √ | ' ' | 操作用户名 |
| 13 | foptime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 14 | fbillpkid | 单据PKID | varchar | 50 |  | √ | ' ' | 单据PKID |
| 15 | ffilename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 16 | furl | 文件url | varchar | 500 |  | √ | ' ' | 文件url |
| 17 | forgname | 操作组织名 | varchar | 128 |  | √ | ' ' | 操作组织名 |
| 18 | fattkey | 附件控件标识 | varchar | 50 |  | √ | ' ' | 附件控件标识 |
| 19 | ffileext | 文件类型 | varchar | 100 |  | √ | ' ' | 文件类型 |
| 20 | fbillno | 单据编号 | varchar | 500 |  | √ | ' ' | 单据编号 |
| 21 | fclient | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_attoplog_billpk |  | fentitynum,fbillpkid |
| 2 | t_bas_attachment_oplog_pkey |  | fid |
| 3 | idx_attoplog_foptime |  | foptime |
| 4 | idx_attoplog_attinfo |  | fattpkid,fatttype |
| 5 | idx_attoplog_fentitynum |  | fentitynum |
