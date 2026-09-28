# 租户配置-ctsy_tenant

## 租户配置-主表 t_ctsy_tenant

- **表名称：** 租户配置-主表
- **表名：** t_ctsy_tenant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | AccessToken加密认证秘钥 | varchar | 200 |  | √ | ' ' | AccessToken加密认证秘钥 |
| 3 | ftenantid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fappid | 第三方应用系统编码 | varchar | 50 |  | √ | ' ' | 第三方应用系统编码 |
| 6 | fstatus | 租户状态 | varchar | 50 |  | √ | 'C' | 租户状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fname | 租户名称 | varchar | 255 |  | √ | ' ' | 租户名称 |
| 10 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fisclinkid | 集成连接配置ID | varchar | 50 |  | √ | ' ' | 集成连接配置ID |
| 12 | faccountnumber | 租户数据中心 | varchar | 50 |  | √ | ' ' | 租户数据中心,枚举: |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fuser | 用户名称 | varchar | 30 |  | √ | ' ' | 用户名称 |
| 15 | fconnecttype | 连接类型 | varchar | 30 |  | √ | ' ' | 连接类型 |
| 16 | fserverip | 访问地址 | varchar | 200 |  | √ | ' ' | 访问地址 |
| 17 | fpwd | 用户登录密码 | varchar | 200 |  | √ | ' ' | 用户登录密码 |
| 18 | fstate | 连接状态 | varchar | 30 |  | √ | ' ' | 连接状态,枚举: F :异常 S :正常 |
| 19 | ftenanttype | 租户属性 | varchar | 30 |  | √ | ' ' | 租户属性,枚举: 0 :集团 1 :公司 2 :分公司 3 :事业部 4 :部门 5 :工厂 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fwebapp | Web应用名 | varchar | 30 |  | √ | ' ' | Web应用名 |
| 22 | fnumber | 租户编码 | varchar | 80 |  | √ | ' ' | 租户编码 |
| 23 | fdeploystate | 部署状态 | varchar | 30 |  | √ | ' ' | 部署状态 |
| 24 | fserverport | 访问端口 | varchar | 30 |  | √ | ' ' | 访问端口 |
| 25 | faccountid | 租户账套ID | varchar | 50 |  | √ | ' ' | 租户账套ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ctsy_tenant_fnumber |  | fnumber |
| 2 | pk_t_ctsy_tenant |  | fid |

---

## 租户配置-多语言表 t_ctsy_tenant_l

- **表名称：** 租户配置-多语言表
- **表名：** t_ctsy_tenant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 租户名称 | varchar | 255 |  | √ | ' ' | 租户名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ctsy_tenant_l_fid |  | fid,flocaleid |
| 2 | pk_t_ctsy_tenant_l |  | fpkid |
